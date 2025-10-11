from PySide6.QtWidgets import QMessageBox, QDialog, QLabel, QVBoxLayout, QWidget
from PySide6.QtGui import QMovie
from PySide6.QtCore import Qt, QSize, QPoint, QUrl
from PySide6.QtNetwork import QNetworkAccessManager, QNetworkRequest, QNetworkReply

from widgets.custom_progress_bar.custom_progress_bar import CustomProgressBar, StepState
from widgets.custom_context_menu.custom_context_menu import CustomContextMenu
from . docker_worker import DockerWorker
from . settings import Settings

class RunProgress:
    def __init__(self, main_window):
        self.main_window = main_window
        self.widgets = main_window.ui
        self.settings = Settings()

        self.widgets.runButton.clicked.connect(self.run_all)
        self.widgets.cleanButton.clicked.connect(self.clean_run)
        self.widgets.pauseButton.clicked.connect(self.pause_run)
        self.widgets.resumeButton.clicked.connect(self.resume_run)

        CustomContextMenu(self.widgets.stdOut)
        self.row_1 = self.widgets.runProgressTab.layout().itemAt(0).widget()
        self.progressbar = CustomProgressBar()
        self.progressbar.set_labels([
            {"label": "Setup Docker", "actions": [("Run", self.start_local_docker)]},
            {"label": "Upload R1 & R2", "actions": [("Run", self.clean_run)]},
            {"label": "QC 1", "actions": [("Run", self.clean_run)]},
            {"label": "UMI", "actions": [("Run", self.clean_run)]},
            {"label": "Cutadapt", "actions": [("Run", self.clean_run)]},
            {"label": "Fastp", "actions": [("Upload", self.pause_run)]},
            {"label": "QC 2", "actions": [("Run QC", self.resume_run), ("Skip", lambda: print("Skipped QC1"))]},
            {"label": "Readlenst", "actions": [("Run QC", self.resume_run), ("Skip", lambda: print("Skipped QC1"))]},
            {"label": "Upload reference genome", "actions": [("Run QC", self.resume_run), ("Skip", lambda: print("Skipped QC1"))]},
            {"label": "Read mapping", "actions": [("Run QC", self.resume_run), ("Skip", lambda: print("Skipped QC1"))]},
            {"label": "Site analysis", "actions": [("Run QC", self.resume_run), ("Skip", lambda: print("Skipped QC1"))]},
        ])
        self.row_1.layout().addWidget(self.progressbar)

    def start_local_docker(self):
        self.progressbar.set_step_state_by_label("Setup Docker", StepState.RUNNING)

        docker_path = self.settings.get("DOCKER_PATH", None)
        if not docker_path:
            self.progressbar.set_step_state_by_label("Setup Docker", StepState.FAILED)
            QMessageBox.critical(
                self.main_window,
                "Docker Error",
                "Docker path not set in settings. Please configure DOCKER_PATH."
            )
            return

        # launch worker thread
        self.docker_worker = DockerWorker(docker_path)
        self.docker_worker.finished.connect(self._on_docker_finished)
        self.docker_worker.start()

    def _on_docker_finished(self, success: bool, error: str, container_id: str, container_ip: str):
        if success:
            self.progressbar.set_step_state_by_label("Setup Docker", StepState.COMPLETED)
            print(container_id);
            print(container_ip);
        else:
            self.progressbar.set_step_state_by_label("Setup Docker", StepState.FAILED)
            QMessageBox.critical(
                self.main_window,
                "Docker Error",
                f"Failed to start Docker container:\n{error}"
            )

    def pause_run(self):
        # Make async HTTP GET request to test connectivity (simulate waiting for backend)
        request = QNetworkRequest(QUrl("https://www.google.com"))
        reply = self.main_window.network_manager.get(request)
        reply.finished.connect(lambda: self.handle_pause_reply(reply))

    def handle_pause_reply(self, reply: QNetworkReply):
        if reply.error() == QNetworkReply.NetworkError.NoError:
            # Successful "ping"
            Settings.METADATA.set("isPaused", True)
        else:
            # Error occurred (no internet or other issue)
            QMessageBox.warning(
                self.main_window,
                "Pause Error",
                f"Failed to reach the server. Error: {reply.errorString()}"
            )

        reply.deleteLater()
        self.load_from_metadata()

    def clean_run(self):
        reply = QMessageBox.question(
            self.main_window,
            "Confirm Cleanup",
            "Are you sure you want to clean this run?\nThis will reset all progress made so far.",
            QMessageBox.Yes | QMessageBox.No
        )

        if reply == QMessageBox.Yes:
            Settings.METADATA.set("isRunning", False)
            self.progressbar.reset()
            self.load_from_metadata()

    def run_all(self):
        Settings.METADATA.set("isRunning", True)
        self.load_from_metadata()

    def resume_run(self):
        Settings.METADATA.set("isPaused", False)
        self.load_from_metadata()

    def load_from_metadata(self):
        is_running = Settings.METADATA.get("isRunning", False)
        is_paused = Settings.METADATA.get("isPaused", False)

        if is_running:
            self.widgets.runButton.hide()
            self.widgets.cleanButton.show()

            if is_paused:
                self.widgets.pauseButton.hide()
                self.widgets.resumeButton.show()
            else:
                self.widgets.pauseButton.show()
                self.widgets.resumeButton.hide()
        else:
            self.widgets.runButton.show()
            self.widgets.pauseButton.hide()
            self.widgets.resumeButton.hide()
            self.widgets.cleanButton.hide()
