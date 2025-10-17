from PySide6.QtNetwork import (
    QNetworkAccessManager, QNetworkRequest, QHttpMultiPart, QHttpPart
)
from PySide6.QtCore import QUrl, QByteArray, QIODevice, Signal, QObject, QTimer
from PySide6.QtWidgets import QMessageBox
from PySide6.QtGui import QTextCursor
import os, json
from .settings import Settings

class APICaller(QObject):
    api_result = Signal(dict)  # {"endpoint": str, "success": bool, "error": str|None, "data": dict|None}

    def __init__(self):
        super().__init__()
        self.manager = QNetworkAccessManager()
        self._buffers = {}
        self._active_logs = set()  # Track logs used by in-flight requests

        self.std_out = None
        self.main_window = None
        self.log_path = None
        self.log_file = None
        self.last_pos = 0

        # Timer to periodically update stdout from log
        self._update_timer = QTimer()
        self._update_timer.setInterval(50)
        self._update_timer.timeout.connect(self._update_stdout_from_log)
        self._update_timer.start()

    def attach_run(self, run, std_out_widget, main_window):
        """Attach or switch APICaller to a specific run."""
        self.std_out = std_out_widget
        self.main_window = main_window
        new_log_path = os.path.join(Settings.RUNS_DIR, run, "log.txt")
        os.makedirs(os.path.dirname(new_log_path), exist_ok=True)

        # Close previous log file only if no active requests are using it
        if self.log_file and self.log_file not in self._active_logs:
            self.log_file.close()

        self.log_path = new_log_path
        self.log_file = open(self.log_path, "a", encoding="utf-8")
        self.last_pos = 0

    def cleanup_run(self):
        """Close and delete the currently attached run's log file."""
        if self.log_file:
            try:
                self.log_file.close()
            except Exception:
                pass
            try:
                if self.log_path and os.path.exists(self.log_path):
                    os.remove(self.log_path)
            except Exception as e:
                print(f"Failed to delete log file {self.log_path}: {e}")
            finally:
                self.log_file = None
                self.log_path = None
                self.last_pos = 0

    def get_base_url(self):
        port = Settings.METADATA.get("docker_host_port", None)
        if not port:
            raise RuntimeError("docker_host_port is not set in metadata!")
        return f"http://127.0.0.1:{port}"

    def stream_api(self, endpoint, method="GET", json_data=None, files=None):
        if not self.log_file:
            raise RuntimeError("APICaller is not attached to any run!")

        log_file = self.log_file
        self._active_logs.add(log_file)

        self._write_to_log(log_file, f"[RUNNING] {endpoint}...")

        url = QUrl(f"{self.get_base_url()}/{endpoint}")
        request = QNetworkRequest(url)

        if files:
            multi_part = QHttpMultiPart(QHttpMultiPart.FormDataType)
            for key, file_obj in files.items():
                if not file_obj.isOpen():
                    file_obj.open(QIODevice.ReadOnly)
                part = QHttpPart()
                part.setHeader(
                    QNetworkRequest.KnownHeaders.ContentDispositionHeader,
                    f'form-data; name="{key}"; filename="{os.path.basename(file_obj.fileName())}"'
                )
                part.setBodyDevice(file_obj)
                file_obj.setParent(multi_part)
                multi_part.append(part)
            reply = self.manager.post(request, multi_part)
            reply.multi_part = multi_part
        elif json_data:
            data = QByteArray(json.dumps(json_data).encode())
            request.setHeader(QNetworkRequest.KnownHeaders.ContentTypeHeader, "application/json")
            reply = self.manager.post(request, data)
        else:
            reply = self.manager.get(request)

        rid = id(reply)
        self._buffers[rid] = ""

        # Only pass log_file; std_out is no longer used
        reply.readyRead.connect(lambda rid=rid, r=reply: self._on_ready_read(rid, r, endpoint, log_file))
        reply.finished.connect(lambda rid=rid, r=reply: self._on_finished(rid, r, endpoint, log_file))

    def _on_ready_read(self, rid, reply, endpoint, log_file):
        buf = self._buffers.setdefault(rid, "")
        chunk = reply.readAll().data().decode(errors="ignore")
        if not chunk:
            return
        buf += chunk

        while "\n" in buf:
            line, buf = buf.split("\n", 1)
            line = line.strip()
            if not line:
                continue

            self._write_to_log(log_file, line)

            if line.startswith("[RESULT]"):
                try:
                    json_part = line[len("[RESULT]"):].strip()
                    result_data = json.loads(json_part)
                except Exception as e:
                    result_data = {
                        "endpoint": endpoint,
                        "success": False,
                        "error": f"Malformed [RESULT]: {e}",
                        "data": None
                    }

                self.api_result.emit(result_data)

        self._buffers[rid] = buf

    def _on_finished(self, rid, reply, endpoint, log_file):
        status_code = reply.attribute(QNetworkRequest.HttpStatusCodeAttribute)
        ok = status_code == 200
        buf = self._buffers.pop(rid, "").strip()
        if buf:
            self._write_to_log(log_file, buf)

        reply.deleteLater()

        if not ok:
            msg = f"{endpoint} returned HTTP {status_code or 'Unknown'}"
            self._write_to_log(log_file, f"❌ {msg}")
            self._safe_message(f"{endpoint} failed", msg)
            self.api_result.emit({
                "endpoint": endpoint,
                "success": False,
                "error": msg,
                "data": None
            })

        self._write_to_log(log_file, f"[DONE] {endpoint} request finished.")

        # Remove from active logs; close if it’s an old run
        self._active_logs.discard(log_file)
        if log_file != self.log_file:
            log_file.close()

    def _write_to_log(self, log_file, line):
        try:
            log_file.write(line + "\n")
            log_file.flush()
        except Exception as e:
            print("Error writing to log:", e)

    def _safe_message(self, title, text):
        if self.main_window:
            QTimer.singleShot(0, lambda: QMessageBox.critical(self.main_window, title, text))

    def _update_stdout_from_log(self):
        if not self.std_out or not self.log_path:
            return
        try:
            with open(self.log_path, "r", encoding="utf-8") as f:
                f.seek(self.last_pos)
                new_data = f.read()
                self.last_pos = f.tell()

            if not new_data:
                return

            cursor = self.std_out.textCursor()
            cursor.movePosition(QTextCursor.MoveOperation.End)
            cursor.insertText(new_data)
            self.std_out.setTextCursor(cursor)
            self.std_out.ensureCursorVisible()

            # Limit output to last 2000 lines
            block_count = self.std_out.document().blockCount()
            if block_count > 2000:
                cursor.movePosition(QTextCursor.MoveOperation.Start)
                cursor.movePosition(QTextCursor.MoveOperation.Down, QTextCursor.KeepAnchor, block_count - 2000)
                cursor.removeSelectedText()
                cursor.deleteChar()

        except Exception as e:
            self._write_to_log(self.log_file, f"[ERROR] Updating stdout from log: {e}")
