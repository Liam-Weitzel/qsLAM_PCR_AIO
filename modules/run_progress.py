from PySide6.QtWidgets import QMessageBox
from widgets.custom_progress_bar.custom_progress_bar import CustomProgressBar, StepState
from widgets.custom_context_menu.custom_context_menu import CustomContextMenu
from .docker_worker import AsyncDockerWorker, DockerManager
from .settings import Settings
from .api_caller import APICaller
from PySide6.QtCore import QFile

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
            {"label": "Setup Docker", "actions": [("(Re)start docker", self.start_local_docker), ("Stop", self.stop_local_docker)]},
            {"label": "Upload R1 & R2", "actions": [("(Re)upload R1 & R2", self.upload_r1_and_r2)]},
            {"label": "QC 1", "actions": [("(Re)run quality control check 1", self.run_qc_one)]},
            {"label": "UMI Tools", "actions": [("(Re)run UMI Tools", self.run_umi)]},
            {"label": "Cutadapt", "actions": [("(Re)run Cutadapt", self.run_cutadapt)]},
            {"label": "Fastp", "actions": [("(Re)run Fastp", self.run_fastp)]},
            {"label": "QC 2", "actions": [("(Re)run quality control check 2", self.run_qc_two)]},
            {"label": "Read length", "actions": [("(Re)read length", self.read_length)]},
            {"label": "Read mapping", "actions": [("(Re)read mapping", self.read_mapping)]},
            {"label": "Site analysis", "actions": [("(Re)run site analysis", self.run_site_analysis)]}
        ])
        self.row_1.layout().addWidget(self.progressbar)

        self.api_caller = APICaller(self.widgets.stdOut)
        self.load_from_metadata()

    def upload_r1_and_r2(self):
        r1_path = Settings.METADATA.get("r1", "")
        r2_path = Settings.METADATA.get("r2", "")

        r1_file = QFile(r1_path)
        r2_file = QFile(r2_path)

        if not r1_file.open(QFile.ReadOnly):
            self.widgets.stdOut.append(f"[ERROR] Failed to open {r1_path}")
            return
        if not r2_file.open(QFile.ReadOnly):
            self.widgets.stdOut.append(f"[ERROR] Failed to open {r2_path}")
            r1_file.close()
            return

        files = {"R1": r1_file, "R2": r2_file}
        self.api_caller.stream_api("upload_r1_r2", method="POST", files=files)

    def run_qc_one(self):
        payload = {"stage": "before"}
        self.api_caller.stream_api("qc", method="POST", json_data=payload)
    
    def run_umi(self):
        self.api_caller.stream_api("umi", method="GET")

    def run_cutadapt(self):
        payload = {
            "r1_seq": Settings.METADATA.get("cutadapt_r1_sequence", ""),
            "r1_error_rate": float(Settings.METADATA.get("cutadapt_r1_error_rate", 0.3)),
            "r1_trim_leading_trailing": int(Settings.METADATA.get("cutadapt_r1_trim_leading", 0)),
            "r1_anchored": Settings.METADATA.get("cutadapt_r1_anchored", False),
            "r1_min_overlap": int(Settings.METADATA.get("cutadapt_r1_min_overlap", 5)),
            "r1_pair_filter": "both",
            "r1_minimum_length_of_read": int(Settings.METADATA.get("cutadapt_r1_min_length", 30)),
            "r2_seq": Settings.METADATA.get("cutadapt_r2_sequence", ""),
            "r2_error_rate": float(Settings.METADATA.get("cutadapt_r2_error_rate", 0.1)),
            "r2_trim_leading_trailing": int(Settings.METADATA.get("cutadapt_r2_trim_leading", 0)),
            "r2_anchored": Settings.METADATA.get("cutadapt_r2_anchored", False),
            "r2_min_overlap": int(Settings.METADATA.get("cutadapt_r2_min_overlap", 10)),
            "r2_pair_filter": "both",
            "r2_minimum_length_of_read": int(Settings.METADATA.get("cutadapt_r2_min_length", 30)),
        }
        self.api_caller.stream_api("cutadapt", method="POST", json_data=payload)

    def run_fastp(self):
        self.api_caller.stream_api("fastp", method="GET")

    def run_qc_two(self):
        payload = {"stage": "after"}
        self.api_caller.stream_api("qc", method="POST", json_data=payload)

    def read_length(self):
        self.api_caller.stream_api("readlen", method="GET")

    def read_mapping(self):
        genome = Settings.METADATA.get("reference_genome", "")
        tar_url = Settings.METADATA.get("reference_genome_url", None)

        payload = {"genome": genome, "tar_url": tar_url}

        self.api_caller.stream_api("read_mapping", method="POST", json_data=payload)

    def run_site_analysis(self):
        payload = {
            "genome": Settings.METADATA.get("reference_genome", ""),
            "promoter.left": Settings.METADATA.get("promoter.left", "5000"),
            "promoter.right": Settings.METADATA.get("promoter.right", "2000"),
            "enhancer.left": Settings.METADATA.get("enhancer.left", "50000")
        }

        self.api_caller.stream_api("site_analysis", method="POST", json_data=payload)

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
        self.progressbar.reset()
        self.load_from_metadata()

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
            self.docker_worker = AsyncDockerWorker(
                DockerManager.clean_container,
                Settings.METADATA.get("docker_container_id", "")
            )
            self.docker_worker.finished.connect(self._on_docker_cleaned)
            self.docker_worker.start()

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
