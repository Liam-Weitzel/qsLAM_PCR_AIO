import os
from datetime import datetime
from PySide6.QtWidgets import QMessageBox
from widgets.custom_progress_bar.custom_progress_bar import CustomProgressBar, StepState
from widgets.custom_context_menu.custom_context_menu import CustomContextMenu
from .docker_worker import AsyncDockerWorker, DockerManager
from .settings import Settings
from .api_caller import APICaller
from .metadata import Metadata
from PySide6.QtCore import QFile, QTimer

class RunProgress:
    def __init__(self, main_window):
        self.main_window = main_window
        self.widgets = main_window.ui
        self.settings = Settings()

        # Initialize worker references
        self.docker_worker = None
        self.ping_worker = None

        self.widgets.runButton.clicked.connect(self.run_all)
        self.widgets.cleanButton.clicked.connect(self.clean_run)
        self.widgets.pauseButton.clicked.connect(self.pause_run)
        self.widgets.resumeButton.clicked.connect(self.resume_run)

        CustomContextMenu(self.widgets.stdOut)
        self.row_1 = self.widgets.runProgressTab.layout().itemAt(0).widget()
        self.progressbar = CustomProgressBar()
        # Initialize with default steps - will be updated when metadata loads
        self._update_pipeline_steps()
        # Connect progress bar state changes to metadata persistence
        self.progressbar.stepStateChangedForRun.connect(self._save_step_state_to_metadata)
        # Connect progress bar state changes to button state refresh
        self.progressbar.stepStateChangedForRun.connect(self._on_step_state_changed_for_run)

        self.row_1.layout().addWidget(self.progressbar)
        self.api_caller = APICaller()

        # Connect to API completion signals
        self.api_caller.run_step_completed.connect(self._on_step_completed)

        # Pipeline auto-run state - will be populated by _update_pipeline_steps()
        self._pipeline_steps = []

        # Mapping from API endpoints to progress bar step labels
        self.endpoint_to_step = {
            "upload_r1_r2": "Upload R1 & R2",
            "qc": lambda stage: "QC 1" if stage == "before" else "QC 2",
            "umi": "UMI Tools",
            "cutadapt": "Cutadapt",
            "fastp": "Fastp",
            "readlen": "Read length",
            "read_mapping": "Read mapping",
            "site_analysis": "Site analysis",
            "get_results": "Download results"
        }

    def __del__(self):
        """Ensure proper cleanup when object is destroyed."""
        try:
            self._cleanup_workers()
        except:
            pass

    def _save_step_state_to_metadata(self, run_name: str, step_label: str, state_name: str):
        """Save step state to the specific run's metadata."""
        try:
            metadata = Metadata(run_name)
            step_states = metadata.get("step_states", {})
            step_states[step_label] = state_name
            metadata.set("step_states", step_states)
        except Exception as e:
            print(f"[ERROR] Failed to save step state for run {run_name}: {e}")

    def _on_step_state_changed_for_run(self, run_name: str, step_label: str, state_name: str):
        """Handle step state changes and refresh UI button states if this is the current run."""
        # Only refresh button states if this state change is for the currently selected run
        if run_name == Settings.SELECTED_RUN:
            self._update_button_states()

    def _get_enabled_pipeline_steps(self, metadata=None):
        """Get the list of enabled pipeline steps based on configuration flags.
        Returns list of dicts with label and actions for progress bar.
        """
        # All possible steps with their configuration flags
        all_steps = [
            {
                "label": "Setup Docker",
                "actions": [("(Re)start docker", self.start_local_docker), ("Stop", self.stop_local_docker)],
                "always_enabled": True
            },
            {
                "label": "Upload R1 & R2",
                "actions": [("(Re)upload R1 & R2", self.upload_r1_and_r2)],
                "always_enabled": True
            },
            {
                "label": "QC 1",
                "actions": [("(Re)run quality control check 1", self.run_qc_one)],
                "config_flag": "qc_before"
            },
            {
                "label": "UMI Tools",
                "actions": [("(Re)run UMI Tools", self.run_umi)],
                "config_flag": "umi_enabled"
            },
            {
                "label": "Cutadapt",
                "actions": [("(Re)run Cutadapt", self.run_cutadapt)],
                "config_flag": "cutadapt_use"
            },
            {
                "label": "Fastp",
                "actions": [("(Re)run Fastp", self.run_fastp)],
                "always_enabled": True
            },
            {
                "label": "QC 2",
                "actions": [("(Re)run quality control check 2", self.run_qc_two)],
                "config_flag": "qc_after"
            },
            {
                "label": "Read length",
                "actions": [("(Re)read length", self.read_length)],
                "config_flag": "read_len"
            },
            {
                "label": "Read mapping",
                "actions": [("(Re)read mapping", self.read_mapping)],
                "always_enabled": True
            },
            {
                "label": "Site analysis",
                "actions": [("(Re)run site analysis", self.run_site_analysis)],
                "always_enabled": True
            },
            {
                "label": "Download results",
                "actions": [("(Re)download results", self.download_results)],
                "always_enabled": True
            }
        ]

        enabled_steps = []

        for step in all_steps:
            # Always include steps that are always enabled
            if step.get("always_enabled", False):
                enabled_steps.append({"label": step["label"], "actions": step["actions"]})
            elif "config_flag" in step and metadata:
                # Include optional steps if they're enabled in configuration
                if metadata.get(step["config_flag"], False):
                    enabled_steps.append({"label": step["label"], "actions": step["actions"]})
            elif not metadata:
                # If no metadata available, include all steps (fallback behavior)
                enabled_steps.append({"label": step["label"], "actions": step["actions"]})

        return enabled_steps

    def _get_enabled_pipeline_step_functions(self, metadata=None):
        """Get the list of enabled pipeline step functions for auto-run navigation.
        Returns list of tuples (label, function).
        """
        # All possible steps with their functions
        all_step_functions = [
            ("Setup Docker", self.start_local_docker, True),  # always_enabled
            ("Upload R1 & R2", self.upload_r1_and_r2, True),  # always_enabled
            ("QC 1", self.run_qc_one, "qc_before"),
            ("UMI Tools", self.run_umi, "umi_enabled"),
            ("Cutadapt", self.run_cutadapt, "cutadapt_use"),
            ("Fastp", self.run_fastp, True),  # always_enabled
            ("QC 2", self.run_qc_two, "qc_after"),
            ("Read length", self.read_length, "read_len"),
            ("Read mapping", self.read_mapping, True),  # always_enabled
            ("Site analysis", self.run_site_analysis, True),  # always_enabled
            ("Download results", self.download_results, True)  # always_enabled
        ]

        enabled_step_functions = []

        for label, func, config_flag in all_step_functions:
            if config_flag is True:  # Always enabled
                enabled_step_functions.append((label, func))
            elif isinstance(config_flag, str) and metadata:
                # Include optional steps if they're enabled in configuration
                if metadata.get(config_flag, False):
                    enabled_step_functions.append((label, func))
            elif not metadata:
                # If no metadata available, include all steps (fallback behavior)
                enabled_step_functions.append((label, func))

        return enabled_step_functions

    def _update_pipeline_steps(self, metadata=None):
        """Update both progress bar steps and internal pipeline steps based on configuration."""
        enabled_steps = self._get_enabled_pipeline_steps(metadata)
        self.progressbar.set_labels(enabled_steps)

        # Update internal pipeline steps for auto-run navigation
        self._pipeline_steps = self._get_enabled_pipeline_step_functions(metadata)

    def _get_current_run_and_metadata(self):
        """Helper to get current run and its metadata. Returns (run_name, metadata) or (None, None) on error."""
        current_run = Settings.SELECTED_RUN
        if not current_run:
            return None, None

        try:
            metadata = Metadata(current_run)
            return current_run, metadata
        except Exception as e:
            print(f"[ERROR] Failed to load metadata for run {current_run}: {e}")
            return None, None

    def _has_any_step_executed(self, metadata):
        """Check if any step has been executed (not INACTIVE)."""
        step_states = metadata.get("step_states", {})
        for step_label, _ in self._pipeline_steps:
            state = step_states.get(step_label, "INACTIVE")
            if state != "INACTIVE":
                return True
        return False

    def _is_docker_step_running(self):
        """Check if the Setup Docker step is currently RUNNING."""
        current_run, metadata = self._get_current_run_and_metadata()
        if not current_run:
            return False

        step_states = metadata.get("step_states", {})
        docker_state = step_states.get("Setup Docker", "INACTIVE")
        return docker_state == "RUNNING"

    def _get_step_label_for_endpoint(self, endpoint: str, run_name: str) -> str:
        """Get the progress bar step label for an API endpoint."""
        if endpoint == "qc":
            # For QC, we need to check the metadata to see if it's before or after
            try:
                metadata = Metadata(run_name)
                stage = metadata.get("stage", "before")
                step_label = "QC 1" if stage == "before" else "QC 2"

                # Verify the step is currently enabled
                current_steps = [step["label"] for step in self._get_enabled_pipeline_steps(metadata)]
                return step_label if step_label in current_steps else None
            except Exception:
                return "QC 1"  # fallback

        step_mapping = self.endpoint_to_step.get(endpoint)
        if callable(step_mapping):
            step_label = step_mapping()
        else:
            step_label = step_mapping or endpoint

        # Verify the step is currently enabled for this run
        try:
            metadata = Metadata(run_name)
            current_steps = [step["label"] for step in self._get_enabled_pipeline_steps(metadata)]
            return step_label if step_label in current_steps else None
        except Exception:
            return step_label  # fallback if metadata can't be loaded

    def _on_step_completed(self, run_name: str, endpoint: str, success: bool, error_msg: str):
        """Handle completion of an API step."""
        # Race condition protection: Check if the run still has a valid Docker container
        # If clean was called, the container info will be cleared from metadata
        try:
            metadata = Metadata(run_name)
            container_id = metadata.get("docker_container_id", None)
            container_owner = metadata.get("docker_container_owner", None)

            # If no container or container ownership changed, ignore this completion callback
            if not container_id or container_owner != run_name:
                print(f"[INFO] Step completion for {run_name}/{endpoint} ignored - container state invalid")
                return
        except Exception as e:
            print(f"[ERROR] Failed to validate container state for {run_name}: {e}")
            return

        step_label = self._get_step_label_for_endpoint(endpoint, run_name)

        # If step is no longer enabled/visible, ignore the completion callback
        if step_label is None:
            print(f"[INFO] Step completion for {run_name}/{endpoint} ignored - step not currently enabled")
            return

        if success:
            self.progressbar.set_step_state_for_run(run_name, step_label, StepState.COMPLETED)

            # Update last run timestamp for successful steps
            try:
                metadata = Metadata(run_name)
                current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                metadata.set("last_run_timestamp", current_time)
            except Exception as e:
                print(f"[ERROR] Failed to update last_run_timestamp for {run_name}: {e}")

            # Continue auto-run if this is the current run and we're in auto-run mode
            if run_name == Settings.SELECTED_RUN:
                self._continue_auto_run(run_name, step_label)
        else:
            self.progressbar.set_step_state_for_run(run_name, step_label, StepState.FAILED)

            # Auto-pause on failure if in auto-run mode
            if run_name == Settings.SELECTED_RUN:
                self._auto_pause_on_failure(run_name, step_label)

            # Show error popup on separate thread
            QTimer.singleShot(0, lambda: self._show_error_popup(run_name, step_label, error_msg))

    def _show_error_popup(self, run_name: str, step_label: str, error_msg: str):
        """Show critical error popup with run and step context."""
        title = f"Step Failed - {step_label}"
        message = f"Run: {run_name}\nStep: {step_label}\n\nError: {error_msg}"

        QMessageBox.critical(
            self.main_window,
            title,
            message
        )

    def _handle_upload_error(self, run_name: str, error_msg: str):
        """Handle upload validation errors by setting step to failed and triggering auto-pause."""
        step_label = "Upload R1 & R2"

        # Set step state to FAILED
        self.progressbar.set_step_state_for_run(run_name, step_label, StepState.FAILED)

        # Auto-pause if in auto-run mode
        self._auto_pause_on_failure(run_name, step_label)

        # Show error popup
        QTimer.singleShot(0, lambda: self._show_error_popup(run_name, step_label, error_msg))

        # Also log to stdout
        self.widgets.stdOut.append(f"[ERROR] {error_msg}")

    def _is_auto_run_active(self, run_name: str) -> bool:
        """Check if auto-run mode is active for a specific run."""
        try:
            metadata = Metadata(run_name)
            return metadata.get("isAutoRun", False) and not metadata.get("isPaused", False)
        except Exception:
            return False

    def _continue_auto_run(self, run_name: str, completed_step: str):
        """Continue auto-run pipeline to the next step."""
        if not self._is_auto_run_active(run_name):
            return

        # Find the next step to execute
        next_step_func = self._get_next_step(completed_step)
        if next_step_func:
            # Small delay to ensure UI updates, then execute next step
            QTimer.singleShot(100, next_step_func)
        else:
            # Pipeline completed, stop auto-run
            self._stop_auto_run(run_name)

    def _auto_pause_on_failure(self, run_name: str, failed_step: str):
        """Auto-pause the pipeline when a step fails."""
        try:
            metadata = Metadata(run_name)
            if metadata.get("isAutoRun", False):
                metadata.set("isPaused", True)
                metadata.set("lastFailedStep", failed_step)
                print(f"Auto-paused pipeline for run {run_name} after {failed_step} failed")
                # Refresh UI if this is the current run
                if run_name == Settings.SELECTED_RUN:
                    self._update_button_states()
        except Exception as e:
            print(f"[ERROR] Failed to auto-pause run {run_name}: {e}")

    def _get_next_step(self, completed_step: str):
        """Get the next step function to execute after the completed step."""
        step_labels = [step[0] for step in self._pipeline_steps]
        try:
            current_index = step_labels.index(completed_step)
            if current_index + 1 < len(self._pipeline_steps):
                return self._pipeline_steps[current_index + 1][1]
        except ValueError:
            pass
        return None

    def _get_step_function(self, step_label: str):
        """Get the function for a specific step label."""
        for label, func in self._pipeline_steps:
            if label == step_label:
                return func
        return None

    def _stop_auto_run(self, run_name: str):
        """Stop auto-run mode for a specific run."""
        try:
            metadata = Metadata(run_name)
            metadata.set("isAutoRun", False)
            metadata.set("isPaused", False)
            metadata.delete("lastFailedStep")
            print(f"Pipeline completed for run {run_name}")
            # Refresh UI if this is the current run
            if run_name == Settings.SELECTED_RUN:
                self._update_button_states()
        except Exception as e:
            print(f"[ERROR] Failed to stop auto-run for run {run_name}: {e}")

    def _update_button_states(self):
        """Lightweight method to update only button states without full metadata reload."""
        current_run, metadata = self._get_current_run_and_metadata()
        if not current_run:
            self.widgets.runButton.setVisible(False)
            self.widgets.cleanButton.setVisible(False)
            self.widgets.pauseButton.setVisible(False)
            self.widgets.resumeButton.setVisible(False)
            return

        is_running = metadata.get("isRunning", False)
        is_paused = metadata.get("isPaused", False)
        is_auto_run = metadata.get("isAutoRun", False)
        has_executed_steps = self._has_any_step_executed(metadata)

        # Update button states only
        self.widgets.runButton.setVisible(not is_running)
        self.widgets.pauseButton.setVisible(is_running and is_auto_run and not is_paused)
        self.widgets.resumeButton.setVisible(is_running and is_auto_run and is_paused)
        # Show clean button if any steps have been executed (not just when isRunning)
        self.widgets.cleanButton.setVisible(has_executed_steps)
        # Disable clean button only when Docker step is RUNNING (since clean requires stopping Docker)
        self.widgets.cleanButton.setEnabled(not self._is_docker_step_running())

    def upload_r1_and_r2(self):
        current_run, metadata = self._get_current_run_and_metadata()
        if not current_run:
            return

        # Validate file paths before setting step to RUNNING
        r1_path = metadata.get("r1", "")
        r2_path = metadata.get("r2", "")

        # Check if paths are provided
        if not r1_path or not r2_path:
            error_msg = "R1 and R2 file paths must be configured before upload"
            self._handle_upload_error(current_run, error_msg)
            return

        # Check if files exist
        if not os.path.exists(r1_path):
            error_msg = f"R1 file not found: {r1_path}"
            self._handle_upload_error(current_run, error_msg)
            return

        if not os.path.exists(r2_path):
            error_msg = f"R2 file not found: {r2_path}"
            self._handle_upload_error(current_run, error_msg)
            return

        # Now safe to set to RUNNING since validation passed
        self.progressbar.set_step_state_for_run(current_run, "Upload R1 & R2", StepState.RUNNING)

        r1_file = QFile(r1_path)
        r2_file = QFile(r2_path)

        if not r1_file.open(QFile.ReadOnly):
            error_msg = f"Failed to open R1 file: {r1_path} (check permissions)"
            self._handle_upload_error(current_run, error_msg)
            return

        if not r2_file.open(QFile.ReadOnly):
            r1_file.close()
            error_msg = f"Failed to open R2 file: {r2_path} (check permissions)"
            self._handle_upload_error(current_run, error_msg)
            return

        files = {"R1": r1_file, "R2": r2_file}
        self.api_caller.stream_api_for_run(current_run, "upload_r1_r2", method="POST", files=files)

    def run_qc_one(self):
        current_run, metadata = self._get_current_run_and_metadata()
        if not current_run:
            return

        self.progressbar.set_step_state_for_run(current_run, "QC 1", StepState.RUNNING)
        payload = {"stage": "before"}
        metadata.set("stage", "before")
        self.api_caller.stream_api_for_run(current_run, "qc", method="POST", json_data=payload)

    def run_umi(self):
        current_run, metadata = self._get_current_run_and_metadata()
        if not current_run:
            return

        self.progressbar.set_step_state_for_run(current_run, "UMI Tools", StepState.RUNNING)
        self.api_caller.stream_api_for_run(current_run, "umi", method="GET")

    def run_cutadapt(self):
        current_run, metadata = self._get_current_run_and_metadata()
        if not current_run:
            return

        self.progressbar.set_step_state_for_run(current_run, "Cutadapt", StepState.RUNNING)
        payload = {
            "r1_seq": metadata.get("cutadapt_r1_sequence", ""),
            "r1_error_rate": float(metadata.get("cutadapt_r1_error_rate", 0.3)),
            "r1_trim_leading_trailing": int(metadata.get("cutadapt_r1_trim_leading", 0)),
            "r1_anchored": metadata.get("cutadapt_r1_anchored", False),
            "r1_min_overlap": int(metadata.get("cutadapt_r1_min_overlap", 5)),
            "r1_pair_filter": "both",
            "r1_minimum_length_of_read": int(metadata.get("cutadapt_r1_min_length", 30)),
            "r2_seq": metadata.get("cutadapt_r2_sequence", ""),
            "r2_error_rate": float(metadata.get("cutadapt_r2_error_rate", 0.1)),
            "r2_trim_leading_trailing": int(metadata.get("cutadapt_r2_trim_leading", 0)),
            "r2_anchored": metadata.get("cutadapt_r2_anchored", False),
            "r2_min_overlap": int(metadata.get("cutadapt_r2_min_overlap", 10)),
            "r2_pair_filter": "both",
            "r2_minimum_length_of_read": int(metadata.get("cutadapt_r2_min_length", 30)),
        }
        self.api_caller.stream_api_for_run(current_run, "cutadapt", method="POST", json_data=payload)

    def run_fastp(self):
        current_run, metadata = self._get_current_run_and_metadata()
        if not current_run:
            return

        self.progressbar.set_step_state_for_run(current_run, "Fastp", StepState.RUNNING)
        self.api_caller.stream_api_for_run(current_run, "fastp", method="GET")

    def run_qc_two(self):
        current_run, metadata = self._get_current_run_and_metadata()
        if not current_run:
            return

        self.progressbar.set_step_state_for_run(current_run, "QC 2", StepState.RUNNING)
        payload = {"stage": "after"}
        metadata.set("stage", "after")
        self.api_caller.stream_api_for_run(current_run, "qc", method="POST", json_data=payload)

    def read_length(self):
        current_run, metadata = self._get_current_run_and_metadata()
        if not current_run:
            return

        self.progressbar.set_step_state_for_run(current_run, "Read length", StepState.RUNNING)
        self.api_caller.stream_api_for_run(current_run, "readlen", method="GET")

    def read_mapping(self):
        current_run, metadata = self._get_current_run_and_metadata()
        if not current_run:
            return

        self.progressbar.set_step_state_for_run(current_run, "Read mapping", StepState.RUNNING)
        genome = metadata.get("reference_genome", "")
        tar_url = metadata.get("reference_genome_url", None)
        payload = {"genome": genome, "tar_url": tar_url}
        self.api_caller.stream_api_for_run(current_run, "read_mapping", method="POST", json_data=payload)

    def run_site_analysis(self):
        current_run, metadata = self._get_current_run_and_metadata()
        if not current_run:
            return

        self.progressbar.set_step_state_for_run(current_run, "Site analysis", StepState.RUNNING)
        payload = {
            "genome": metadata.get("reference_genome", ""),
            "promoter.left": metadata.get("promoter.left", "5000"),
            "promoter.right": metadata.get("promoter.right", "2000"),
            "enhancer.left": metadata.get("enhancer.left", "50000")
        }
        self.api_caller.stream_api_for_run(current_run, "site_analysis", method="POST", json_data=payload)

    def download_results(self):
        current_run, metadata = self._get_current_run_and_metadata()
        if not current_run:
            return

        self.progressbar.set_step_state_for_run(current_run, "Download results", StepState.RUNNING)
        self.api_caller.download_results_for_run(current_run, "get_results")

    def _update_docker_step_status(self):
        current_run, metadata = self._get_current_run_and_metadata()
        if not current_run:
            self.progressbar.set_step_state_by_label("Setup Docker", StepState.INACTIVE)
            return

        container_id = metadata.get("docker_container_id", None)
        host_port = metadata.get("docker_host_port", None)
        container_owner = metadata.get("docker_container_owner", None)

        if container_id:
            # Only show RUNNING/COMPLETED if this run owns the container
            if container_owner != current_run:
                self.progressbar.set_step_state_for_run(current_run, "Setup Docker", StepState.INACTIVE)
                return

            status = DockerManager.get_container_status(container_id)
            if status is None:
                self.progressbar.set_step_state_for_run(current_run, "Setup Docker", StepState.INACTIVE)
            elif status.startswith("Up"):
                self.progressbar.set_step_state_for_run(current_run, "Setup Docker", StepState.RUNNING)
                if host_port:
                    # Only start ping worker if not already running
                    if not (self.ping_worker and self.ping_worker.isRunning()):
                        self.ping_worker = AsyncDockerWorker(
                            DockerManager.wait_for_container_async,
                            host_port,
                            120000,  # timeout
                            1000     # retry interval
                        )
                        self.ping_worker.finished.connect(
                            lambda ok, *_: self._on_docker_ping(ok, container_id, host_port, current_run)
                        )
                        self.ping_worker.start()
                else:
                    # This shouldn't really happen so cleaning the docker container here
                    self.docker_worker = AsyncDockerWorker(
                        DockerManager.clean_container,
                        container_id
                    )
                    self.docker_worker.finished.connect(
                        lambda success, error, cid: self._on_docker_cleaned(success, error, cid, current_run)
                    )
                    self.docker_worker.start()
            else:  # Exited, Created, or other states
                self.progressbar.set_step_state_for_run(current_run, "Setup Docker", StepState.INACTIVE)
        else:
            self.progressbar.set_step_state_for_run(current_run, "Setup Docker", StepState.INACTIVE)

    def _on_docker_cleaned(self, success: bool, error: str, container_id: str, run_name: str):
        if not success:
            self.progressbar.set_step_state_for_run(run_name, "Setup Docker", StepState.FAILED)
            QMessageBox.critical(
                self.main_window,
                "Docker Error",
                f"Failed to clean Docker container:\n{error}"
            )
            return

        try:
            metadata = Metadata(run_name)
            metadata.delete("docker_container_id")
            metadata.delete("docker_host_port")
            metadata.delete("docker_container_owner")  # Clear ownership when container is cleaned
        except Exception as e:
            print(f"[ERROR] Failed to update metadata for run {run_name}: {e}")

        # Only reset if this is the currently selected run
        if Settings.SELECTED_RUN == run_name:
            self.progressbar.reset()
            self.api_caller.cleanup_run()
            self.load_from_metadata()

    def stop_local_docker(self):
        current_run, metadata = self._get_current_run_and_metadata()
        if not current_run:
            return

        # Clean up any existing workers first
        self._cleanup_workers()

        self.progressbar.set_step_state_for_run(current_run, "Setup Docker", StepState.RUNNING)

        container_id = metadata.get("docker_container_id", None)
        self.docker_worker = AsyncDockerWorker(
            DockerManager.stop_container,
            container_id
        )
        self.docker_worker.finished.connect(
            lambda success, error, cid: self._on_docker_stopped(success, error, cid, current_run)
        )
        self.docker_worker.start()

    def _on_docker_stopped(self, success: bool, error: str, container_id: str, run_name: str):
        if not success:
            self.progressbar.set_step_state_for_run(run_name, "Setup Docker", StepState.FAILED)
            QMessageBox.critical(
                self.main_window,
                "Docker Error",
                f"Failed to stop Docker container:\n{error}"
            )
            return

        try:
            metadata = Metadata(run_name)
            metadata.delete("docker_host_port")
            metadata.delete("docker_container_owner")  # Clear ownership when container is stopped
        except Exception as e:
            print(f"[ERROR] Failed to update metadata for run {run_name}: {e}")

        self.progressbar.set_step_state_for_run(run_name, "Setup Docker", StepState.INACTIVE)
        print(f"Docker container {container_id} has been stopped successfully")

    def start_local_docker(self):
        current_run, metadata = self._get_current_run_and_metadata()
        if not current_run:
            return

        # Clean up any existing workers first
        self._cleanup_workers()

        self.progressbar.set_step_state_for_run(current_run, "Setup Docker", StepState.RUNNING)

        container_id = metadata.get("docker_container_id", None)
        self.docker_worker = AsyncDockerWorker(
            DockerManager.run_container,
            "latest",
            container_id  # DockerManager should attempt to start this container first
        )
        self.docker_worker.finished.connect(
            lambda success, error, cid, host_port: self._on_docker_started(success, error, cid, host_port, current_run)
        )
        self.docker_worker.start()

    def _on_docker_started(self, success: bool, error: str, container_id: str, host_port: str, run_name: str):
        if not success:
            self.progressbar.set_step_state_for_run(run_name, "Setup Docker", StepState.FAILED)
            QMessageBox.critical(
                self.main_window,
                "Docker Error",
                f"Failed to start Docker container:\n{error}"
            )
            return

        try:
            metadata = Metadata(run_name)
            metadata.set("docker_container_id", container_id)
            metadata.set("docker_host_port", host_port)
            metadata.set("docker_container_owner", run_name)  # Track which run owns this container
        except Exception as e:
            print(f"[ERROR] Failed to update metadata for run {run_name}: {e}")

        # Start ping worker to wait for container readiness
        self.ping_worker = AsyncDockerWorker(
            DockerManager.wait_for_container_async,
            host_port,
            120000,  # timeout
            1000     # retry interval
        )
        self.ping_worker.finished.connect(
            lambda ok, *_: self._on_docker_ping(ok, container_id, host_port, run_name)
        )
        self.ping_worker.start()

    def _on_docker_ping(self, success: bool, container_id: str, host_port: str, run_name: str):
        # Race condition protection: Validate that this run still owns the container before updating state
        # If clean was called, the container info will be cleared from metadata
        try:
            metadata = Metadata(run_name)
            current_container_id = metadata.get("docker_container_id", None)
            container_owner = metadata.get("docker_container_owner", None)

            # If no container, container ID changed, or ownership changed, ignore this callback
            if not current_container_id or current_container_id != container_id or container_owner != run_name:
                print(f"[INFO] Ping callback for {run_name} ignored - container state invalid")
                return
        except Exception as e:
            print(f"[ERROR] Failed to validate container state for {run_name}: {e}")
            return

        if success:
            self.progressbar.set_step_state_for_run(run_name, "Setup Docker", StepState.COMPLETED)
            print(f"Docker container {container_id} is alive on port {host_port}")

            # Continue auto-run if this is the current run and we're in auto-run mode
            if run_name == Settings.SELECTED_RUN:
                self._continue_auto_run(run_name, "Setup Docker")
        else:
            self.progressbar.set_step_state_for_run(run_name, "Setup Docker", StepState.FAILED)

            # Auto-pause on failure if in auto-run mode
            if run_name == Settings.SELECTED_RUN:
                self._auto_pause_on_failure(run_name, "Setup Docker")

            QMessageBox.critical(
                self.main_window,
                "Docker Error",
                f"Docker container {container_id} did not respond on port {host_port}"
            )

    def pause_run(self):
        current_run, metadata = self._get_current_run_and_metadata()
        if not current_run:
            return

        metadata.set("isPaused", True)
        print(f"Pipeline paused for run {current_run}")
        self._update_button_states()

    def clean_run(self):
        current_run, metadata = self._get_current_run_and_metadata()
        if not current_run:
            return

        reply = QMessageBox.question(
            self.main_window,
            "Confirm Cleanup",
            "Are you sure you want to clean this run?\nThis will reset all progress made so far.",
            QMessageBox.Yes | QMessageBox.No
        )

        if reply == QMessageBox.Yes:
            # Clean up any existing workers first
            self._cleanup_workers()

            metadata.set("isRunning", False)
            metadata.set("isAutoRun", False)
            metadata.set("isPaused", False)
            metadata.delete("lastFailedStep")

            self.docker_worker = AsyncDockerWorker(
                DockerManager.clean_container,
                metadata.get("docker_container_id", "")
            )
            self.docker_worker.finished.connect(
                lambda success, error, cid: self._on_docker_cleaned(success, error, cid, current_run)
            )
            self.docker_worker.start()

    def run_all(self):
        """Start the full pipeline in auto-run mode."""
        current_run, metadata = self._get_current_run_and_metadata()
        if not current_run:
            return

        metadata.set("isRunning", True)
        metadata.set("isAutoRun", True)
        metadata.set("isPaused", False)
        metadata.delete("lastFailedStep")  # Clear any previous failure

        print(f"Starting full pipeline for run {current_run}")
        self.load_from_metadata()

        # Start with the first step
        first_step_func = self._pipeline_steps[0][1]
        QTimer.singleShot(100, first_step_func)

    def resume_run(self):
        """Resume the pipeline from where it left off."""
        current_run, metadata = self._get_current_run_and_metadata()
        if not current_run:
            return

        metadata.set("isPaused", False)
        print(f"Pipeline resumed for run {current_run}")

        # Check if we need to retry a failed step
        failed_step = metadata.get("lastFailedStep")
        if failed_step:
            print(f"Retrying failed step: {failed_step}")
            step_func = self._get_step_function(failed_step)
            if step_func:
                metadata.delete("lastFailedStep")  # Clear the failure
                QTimer.singleShot(100, step_func)
        else:
            # Find the next step after the last completed one
            last_completed = self._find_last_completed_step(current_run)
            if last_completed:
                next_step_func = self._get_next_step(last_completed)
                if next_step_func:
                    QTimer.singleShot(100, next_step_func)
                else:
                    # Pipeline already completed
                    self._stop_auto_run(current_run)

        self._update_button_states()

    def _find_last_completed_step(self, run_name: str) -> str:
        """Find the last completed step in the pipeline."""
        try:
            metadata = Metadata(run_name)
            step_states = metadata.get("step_states", {})

            for step_label, _ in reversed(self._pipeline_steps):
                if step_states.get(step_label) == "COMPLETED":
                    return step_label
        except Exception:
            pass
        return None

    def load_from_metadata(self):
        current_run, metadata = self._get_current_run_and_metadata()
        if not current_run:
            # No run selected, hide all buttons and clear progress bar
            self.widgets.runButton.setVisible(False)
            self.widgets.cleanButton.setVisible(False)
            self.widgets.pauseButton.setVisible(False)
            self.widgets.resumeButton.setVisible(False)
            self.progressbar.reset()
            return

        is_running = metadata.get("isRunning", False)
        is_paused = metadata.get("isPaused", False)
        is_auto_run = metadata.get("isAutoRun", False)
        has_executed_steps = self._has_any_step_executed(metadata)

        # Button visibility based on state
        self.widgets.runButton.setVisible(not is_running)
        self.widgets.pauseButton.setVisible(is_running and is_auto_run and not is_paused)
        self.widgets.resumeButton.setVisible(is_running and is_auto_run and is_paused)

        # Show clean button if any steps have been executed (not just when isRunning)
        self.widgets.cleanButton.setVisible(has_executed_steps)
        # Disable clean button only when Docker step is RUNNING (since clean requires stopping Docker)
        self.widgets.cleanButton.setEnabled(not self._is_docker_step_running())

        # Update pipeline steps based on current metadata configuration
        self._update_pipeline_steps(metadata)

        # Load progress bar state from metadata
        self.progressbar.load_run_state(current_run, metadata.to_dict())

        # Refresh Docker step status
        self._update_docker_step_status()

        # Clear previous stdout
        self.widgets.stdOut.clear()
        # Attach APICaller to current run dynamically
        self.api_caller.attach_run(
            run=current_run,
            std_out_widget=self.widgets.stdOut,
            main_window=self.main_window
        )

    def _cleanup_workers(self):
        """Clean up any running worker threads."""
        if self.docker_worker and self.docker_worker.isRunning():
            self.docker_worker.terminate()
            self.docker_worker = None

        if self.ping_worker and self.ping_worker.isRunning():
            self.ping_worker.terminate()
            self.ping_worker = None

    def on_run_selection_changed(self):
        """Call this method when the selected run changes to refresh the UI."""
        self._cleanup_workers()
        self.load_from_metadata()
