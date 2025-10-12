import subprocess
from PySide6.QtCore import QEventLoop, QTimer, QUrl, QThread, Signal
from PySide6.QtNetwork import QNetworkAccessManager, QNetworkRequest, QNetworkReply
from . settings import Settings

class DockerManager:
    image = "liam0w/qslam_pcr_aio"
    default_tag = "latest"

    @classmethod
    def wait_for_container_async(cls, port: str, timeout_ms: int = 120000, interval_ms: int = 1000) -> bool:
        """
        Retry ping until container responds or timeout is reached.
        Designed to be called inside AsyncDockerWorker.
        """
        import time
        start = time.time()
        timeout_s = timeout_ms / 1000
        interval_s = interval_ms / 1000

        while True:
            if DockerManager.ping_container(port):
                return True
            if time.time() - start > timeout_s:
                return False
            time.sleep(interval_s)

    @classmethod
    def run_container(cls, tag: str | None = None, container_id: str | None = None) -> tuple[bool, str, str, str]:
        """
        Run container detached, return (success, error, container_id, host_port).
        If `container_id` is provided, try to start it first.
        Otherwise, create a new container.
        """
        try:
            docker_path = Settings.get_noself("DOCKER_PATH", "docker")
            image_tag = f"{cls.image}:{tag or cls.default_tag}"

            # Pull image first
            pull_cmd = f'{docker_path} pull {image_tag}'
            subprocess.run(pull_cmd, shell=True, check=True)

            if container_id:
                # Check if container exists
                status = cls.get_container_status(container_id)
                if status:
                    if status.startswith("Exited"):
                        # Container exists but stopped → start it
                        start_cmd = f'{docker_path} start {container_id}'
                        subprocess.run(start_cmd, shell=True, check=True)
                    # Already running or just started, return host port
                    port_cmd = f'{docker_path} port {container_id} 5000'
                    port_result = subprocess.run(port_cmd, shell=True, capture_output=True, text=True, check=True)
                    host_port = port_result.stdout.strip().split(":")[-1]
                    return True, "", container_id, host_port
                # If container ID does not exist, fall through to create new

            # Run new container
            run_cmd = f'{docker_path} run -d -p 127.0.0.1::5000 {image_tag}'
            result = subprocess.run(run_cmd, shell=True, capture_output=True, text=True, check=True)
            new_container_id = result.stdout.strip()

            # Get host port
            port_cmd = f'{docker_path} port {new_container_id} 5000'
            port_result = subprocess.run(port_cmd, shell=True, capture_output=True, text=True, check=True)
            host_port = port_result.stdout.strip().split(":")[-1]

            return True, "", new_container_id, host_port

        except subprocess.CalledProcessError as e:
            return False, e.stderr.strip(), "", ""

    @classmethod
    def get_container_status(cls, container_id: str) -> str | None:
        """Return status string of container or None if not exists."""
        docker_path = Settings.get_noself("DOCKER_PATH", "docker")
        try:
            cmd = f'{docker_path} ps -a --filter id={container_id} --format "{{{{.Status}}}}"'
            result = subprocess.run(cmd, shell=True, capture_output=True, text=True, check=True)
            status = result.stdout.strip()
            return status if status else None
        except subprocess.CalledProcessError:
            return None

    @classmethod
    def stop_container(cls, container_id: str) -> bool:
        status = cls.get_container_status(container_id)
        if status is None:
            # container doesn't exist
            return True
        if status.startswith("Exited"):
            # already stopped
            return True
        try:
            docker_path = Settings.get_noself("DOCKER_PATH", "docker")
            cmd = f'{docker_path} stop {container_id}'
            subprocess.run(cmd, shell=True, check=True)
            return True
        except subprocess.CalledProcessError:
            return False

    @classmethod
    def clean_container(cls, container_id: str) -> bool:
        status = cls.get_container_status(container_id)
        if status is None:
            # container doesn't exist, nothing to remove
            return True
        if not status.startswith("Exited"):
            # must stop first
            cls.stop_container(container_id)
        try:
            docker_path = Settings.get_noself("DOCKER_PATH", "docker")
            cmd = f'{docker_path} rm {container_id}'
            subprocess.run(cmd, shell=True, check=True)
            return True
        except subprocess.CalledProcessError:
            return False

    @staticmethod
    def ping_container(port: str) -> bool:
        """
        Ping http://127.0.0.1:PORT/ once using Qt's QNetworkAccessManager.
        Returns True only if reply finishes successfully.
        """
        loop = QEventLoop()
        manager = QNetworkAccessManager()
        url = QUrl(f"http://127.0.0.1:{port}/")
        request = QNetworkRequest(url)
        reply = manager.get(request)

        reply.finished.connect(loop.quit)
        loop.exec()

        success = reply.error() == QNetworkReply.NetworkError.NoError

        reply.deleteLater()
        manager.deleteLater()
        return success

class AsyncDockerWorker(QThread):
    finished = Signal(bool, str, str, str)  # success, error_msg, container_id/port, extra (like host_port)

    def __init__(self, func, *args, **kwargs):
        """
        func: any DockerManager method
        args, kwargs: arguments to func
        """
        super().__init__()
        self.func = func
        self.args = args
        self.kwargs = kwargs

    def run(self):
        try:
            result = self.func(*self.args, **self.kwargs)
            # Normalize result to (success, error_msg, id_or_port, extra)
            if isinstance(result, tuple):
                self.finished.emit(*result)
            else:  # if function returns just a bool
                self.finished.emit(result, "", "", "")
        except Exception as e:
            self.finished.emit(False, str(e), "", "")
