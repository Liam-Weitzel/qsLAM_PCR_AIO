from PySide6.QtWidgets import QMessageBox
from widgets.custom_progress_bar.custom_progress_bar import CustomProgressBar, StepState
from widgets.custom_context_menu.custom_context_menu import CustomContextMenu
from .docker_worker import AsyncDockerWorker, DockerManager
from .settings import Settings

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
            {"label": "Setup Docker", "actions": [("(Re)Start", self.start_local_docker), ("Stop", self.stop_local_docker)]},
            {"label": "Upload R1 & R2", "actions": [("Run", self.clean_run)]},
            {"label": "QC 1", "actions": [("Run", self.clean_run)]},
            {"label": "UMI", "actions": [("Run", self.clean_run)]},
            {"label": "Cutadapt", "actions": [("Run", self.clean_run)]},
            {"label": "Fastp", "actions": [("Run", self.clean_run)]},
            {"label": "QC 2", "actions": [("Run QC", self.resume_run), ("Skip", lambda: print("Skipped QC2"))]},
            {"label": "Readlenst", "actions": [("Run QC", self.resume_run), ("Skip", lambda: print("Skipped Readlenst"))]},
            {"label": "Upload reference genome", "actions": [("Run QC", self.resume_run), ("Skip", lambda: print("Skipped Ref"))]},
            {"label": "Read mapping", "actions": [("Run QC", self.resume_run), ("Skip", lambda: print("Skipped Mapping"))]},
            {"label": "Site analysis", "actions": [("Run QC", self.resume_run), ("Skip", lambda: print("Skipped Site"))]},
        ])
        self.row_1.layout().addWidget(self.progressbar)

        self.load_from_metadata()
    
    def _update_docker_step_status(self):
        if Settings.METADATA:
            container_id = Settings.METADATA.get("docker_container_id", None)
            host_port = Settings.METADATA.get("docker_host_port", None)
        else:
            container_id = None
            host_port = None

        if container_id:
            status = DockerManager.get_container_status(container_id)
            if status is None:
                self.progressbar.set_step_state_by_label("Setup Docker", StepState.INACTIVE)
            elif status.startswith("Up"):
                self.progressbar.set_step_state_by_label("Setup Docker", StepState.RUNNING)
                if host_port:
                    self.ping_worker = AsyncDockerWorker(
                        DockerManager.wait_for_container_async,
                        host_port,
                        120000,  # timeout
                        1000     # retry interval
                    )
                    self.ping_worker.finished.connect(
                        lambda ok, *_: self._on_docker_ping(ok, container_id, host_port)
                    )
                    self.ping_worker.start()
                else:
                    # This shouldn't really happen so cleaning the docker container here
                    self.docker_worker = AsyncDockerWorker(
                        DockerManager.clean_container,
                        container_id
                    )
                    self.docker_worker.finished.connect(self._on_docker_cleaned)
                    self.docker_worker.start()
            else:  # Exited, Created, or other states
                self.progressbar.set_step_state_by_label("Setup Docker", StepState.INACTIVE)
        else:
            self.progressbar.set_step_state_by_label("Setup Docker", StepState.INACTIVE)

    def _on_docker_cleaned(self, success: bool, error: str, container_id: str):
        if not success:
            self.progressbar.set_step_state_by_label("Setup Docker", StepState.FAILED)
            QMessageBox.critical(
                self.main_window,
                "Docker Error",
                f"Failed to clean Docker container:\n{error}"
            )
            return
        Settings.METADATA.delete("docker_container_id")
        Settings.METADATA.delete("docker_host_port")
        self.progressbar.set_step_state_by_label("Setup Docker", StepState.INACTIVE)

    def stop_local_docker(self):
        self.progressbar.set_step_state_by_label("Setup Docker", StepState.RUNNING)

        container_id = Settings.METADATA.get("docker_container_id", None)
        self.docker_worker = AsyncDockerWorker(
            DockerManager.stop_container,
            container_id
        )
        self.docker_worker.finished.connect(self._on_docker_stopped)
        self.docker_worker.start()

    def _on_docker_stopped(self, success: bool, error: str, container_id: str):
        if not success:
            self.progressbar.set_step_state_by_label("Setup Docker", StepState.FAILED)
            QMessageBox.critical(
                self.main_window,
                "Docker Error",
                f"Failed to stop Docker container:\n{error}"
            )
            return

        # wipe docker host port as this gets bound on startup again
        Settings.METADATA.delete("docker_host_port")
        self.progressbar.set_step_state_by_label("Setup Docker", StepState.INACTIVE)
        print(f"Docker container {container_id} has been stopped successfully")

    def start_local_docker(self):
        self.progressbar.set_step_state_by_label("Setup Docker", StepState.RUNNING)

        container_id = Settings.METADATA.get("docker_container_id", None)
        self.docker_worker = AsyncDockerWorker(
            DockerManager.run_container,
            "latest",
            container_id  # DockerManager should attempt to start this container first
        )
        self.docker_worker.finished.connect(self._on_docker_started)
        self.docker_worker.start()

    def _on_docker_started(self, success: bool, error: str, container_id: str, host_port: str):
        if not success:
            self.progressbar.set_step_state_by_label("Setup Docker", StepState.FAILED)
            QMessageBox.critical(
                self.main_window,
                "Docker Error",
                f"Failed to start Docker container:\n{error}"
            )
            return

        # Save container info in metadata for later reuse
        Settings.METADATA.set("docker_container_id", container_id)
        Settings.METADATA.set("docker_host_port", host_port)

        # Start ping worker to wait for container readiness
        self.ping_worker = AsyncDockerWorker(
            DockerManager.wait_for_container_async,
            host_port,
            120000,  # timeout
            1000     # retry interval
        )
        self.ping_worker.finished.connect(
            lambda ok, *_: self._on_docker_ping(ok, container_id, host_port)
        )
        self.ping_worker.start()

    def _on_docker_ping(self, success: bool, container_id: str, host_port: str):
        if success:
            self.progressbar.set_step_state_by_label("Setup Docker", StepState.COMPLETED)
            print(f"Docker container {container_id} is alive on port {host_port}")
        else:
            self.progressbar.set_step_state_by_label("Setup Docker", StepState.FAILED)
            QMessageBox.critical(
                self.main_window,
                "Docker Error",
                f"Docker container {container_id} did not respond on port {host_port}"
            )

    def pause_run(self):
        Settings.METADATA.set("isPaused", True)
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
        if(Settings.METADATA):
            is_running = Settings.METADATA.get("isRunning", False)
            is_paused = Settings.METADATA.get("isPaused", False)
        else:
            is_running = False
            is_paused = False

        self.widgets.runButton.setVisible(not is_running)
        self.widgets.cleanButton.setVisible(is_running)
        self.widgets.pauseButton.setVisible(is_running and not is_paused)
        self.widgets.resumeButton.setVisible(is_running and is_paused)

        # Always refresh Docker step status
        self._update_docker_step_status()
