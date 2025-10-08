from PySide6.QtCore import QThread, Signal
import subprocess

class DockerWorker(QThread):
    # success flag, error message, container_id, container_ip
    finished = Signal(bool, str, str, str)

    def __init__(self, docker_path: str, parent=None):
        super().__init__(parent)
        self.docker_path = docker_path

    def run(self):
        try:
            cmd = [self.docker_path, "run", "-d", "-p", "127.0.0.1::5000", "qslam_pcr_aio:latest"]
            # NAME="qslam_pcr_aio_1"
            # docker run -d --name "$NAME" -p 127.0.0.1::5000 qslam_pcr_aio:latest
            # PORT=$(docker port "$NAME" 5000 | awk -F: '{print $2}')
            # echo "Container '$NAME' is running at http://127.0.0.1:$PORT"
            # TODO: then talk to it over 127.0.0.1 + the bound port...
            result = subprocess.run(cmd, capture_output=True, text=True, check=True)
            container_id = result.stdout.strip()

            cmd_ip = [
                self.docker_path, "inspect", "-f",
                "{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}",
                container_id
            ]
            ip_result = subprocess.run(cmd_ip, capture_output=True, text=True, check=True)
            container_ip = ip_result.stdout.strip()

            self.finished.emit(True, "", container_id, container_ip)

        except subprocess.CalledProcessError as e:
            self.finished.emit(False, e.stderr, "", "")
