from PySide6.QtNetwork import QNetworkAccessManager, QNetworkRequest, QNetworkReply, QHttpMultiPart, QHttpPart
from PySide6.QtCore import QUrl, QUrl, QByteArray
import os, json
from . settings import Settings
from . metadata import Metadata

class APICaller:
    def __init__(self, std_out_widget):
        self.manager = QNetworkAccessManager()
        self.std_out = std_out_widget

    def get_base_url(self):
        port = Settings.METADATA.get("docker_host_port", None)
        if not port:
            raise RuntimeError("docker_host_port is not set in metadata!")
        return f"http://127.0.0.1:{port}"

    def stream_api(self, endpoint, method="GET", json_data=None, files=None):
        url = QUrl(f"{self.get_base_url()}/{endpoint}")
        request = QNetworkRequest(url)

        if files:
            multi_part = QHttpMultiPart(QHttpMultiPart.FormDataType)
            for key, f in files.items():
                part = QHttpPart()
                filename = os.path.basename(f.fileName())
                part.setHeader(QNetworkRequest.KnownHeaders.ContentDispositionHeader,
                               f'form-data; name="{key}"; filename="{filename}"')
                part.setBodyDevice(f)
                f.setParent(multi_part)
                multi_part.append(part)

            reply = self.manager.post(request, multi_part)
            # 🧠 Keep multipart alive by storing it on the reply
            reply.multi_part = multi_part

        elif json_data:
            data = QByteArray(json.dumps(json_data).encode())
            request.setHeader(QNetworkRequest.KnownHeaders.ContentTypeHeader, "application/json")
            reply = self.manager.post(request, data)

        else:
            reply = self.manager.get(request)

        reply.readyRead.connect(lambda: self._on_ready_read(reply))
        reply.finished.connect(lambda: self._on_finished(reply))

    def _on_ready_read(self, reply):
        chunk = reply.readAll().data().decode(errors="ignore")
        if chunk.strip():
            self.std_out.append(chunk)

    def _on_finished(self, reply):
        reply.deleteLater()
