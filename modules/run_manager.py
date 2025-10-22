import sys, subprocess, os, platform
import zipfile2
import json
from datetime import datetime
from PySide6.QtWidgets import QFileDialog, QMessageBox, QTableWidgetItem
from PySide6.QtCore import QTimer, Qt
from . ui_functions import *
from . settings import Settings
from . metadata import Metadata

class RunManager:
    def __init__(self, main_window):
        self.settings = Settings()
        self.main_window = main_window
        self.widgets = main_window.ui

        # Connect buttons to methods
        self.widgets.createRunButton.clicked.connect(self.create_run)
        self.widgets.deleteRunButton.clicked.connect(self.delete_run)
        self.widgets.exportRunButton.clicked.connect(self.export_run)
        self.widgets.importRunButton.clicked.connect(self.import_run)
        self.widgets.selectRunButton.clicked.connect(self.select_run)
        self.widgets.runsTable.cellDoubleClicked.connect(self.select_run)
        self.widgets.refreshRunButton.clicked.connect(self.update_runs_table)
        self.widgets.openFolderLocationButton.clicked.connect(self.open_folder_location)
        self.widgets.renameRunButton.clicked.connect(self.rename_run)

        # Set first load page and select menu
        self.widgets.stackedWidget.setCurrentWidget(self.widgets.runManagerTab)
        self.widgets.runManagerButton.setStyleSheet(UIFunctions.selectMenu(self.widgets.runManagerButton.styleSheet()))

        # Initially disable run management buttons (will be enabled when a run is selected)
        self.widgets.deleteRunButton.setEnabled(False)
        self.widgets.renameRunButton.setEnabled(False)
        self.widgets.openFolderLocationButton.setEnabled(False)
        self.widgets.exportRunButton.setEnabled(False)

        # Schedule a refresh to fill empty rows once the UI is fully rendered
        QTimer.singleShot(100, self.update_runs_table)

        # Ensure the table is filled with empty rows on resize
        self.main_window.resizeEvent = self.on_resize

    def update_runs_table(self):
        try:
            subdirs = [d for d in os.listdir(Settings.RUNS_DIR) if os.path.isdir(os.path.join(Settings.RUNS_DIR, d))]
        except FileNotFoundError:
            print(f"The directory {Settings.RUNS_DIR} doesn't exist!")
            return

        self.widgets.runsTable.setRowCount(0)

        for subdir_name in subdirs:
            try:
                metadata = Metadata(subdir_name)
            except Exception as e:
                print(f"[RunManager] Skipping run '{subdir_name}': {e}")
                continue

            # Create a new row in the table for this run
            row_position = self.widgets.runsTable.rowCount()
            self.widgets.runsTable.insertRow(row_position)

            # Set the first column with the subdirectory name (run)
            self.widgets.runsTable.setItem(row_position, 0, QTableWidgetItem(subdir_name))

            # Column 1: Creation Timestamp (directly from metadata)
            creation_timestamp = metadata.get('creation_timestamp', 'N/A')
            self.widgets.runsTable.setItem(row_position, 1, QTableWidgetItem(str(creation_timestamp)))

            # Column 2: Progress (calculated from step_states)
            progress_status = self.get_progress_status(metadata)
            self.widgets.runsTable.setItem(row_position, 2, QTableWidgetItem(progress_status))

            # Column 3: Last Run Timestamp (calculated from metadata)
            last_run_timestamp = self.get_last_run_timestamp(metadata)
            self.widgets.runsTable.setItem(row_position, 3, QTableWidgetItem(last_run_timestamp))

        # Fill empty rows to match table's height
        self.fill_empty_rows()

    def get_progress_status(self, metadata):
        """Calculate progress status from step_states"""
        step_states = metadata.get('step_states', {})
        is_running = metadata.get('isRunning', False)
        is_paused = metadata.get('isPaused', False)

        if not step_states:
            return "No steps configured"

        # Count step states
        completed_steps = sum(1 for state in step_states.values() if state == "COMPLETED")
        running_steps = sum(1 for state in step_states.values() if state == "RUNNING")
        total_steps = len(step_states)

        # Determine status
        if is_running and running_steps > 0:
            if is_paused:
                # Find the currently running step
                running_step = next((step for step, state in step_states.items() if state == "RUNNING"), "Unknown")
                return f"Paused on: {running_step}"
            else:
                # Find the currently running step
                running_step = next((step for step, state in step_states.items() if state == "RUNNING"), "Unknown")
                return f"Running: {running_step}"
        elif completed_steps == total_steps:
            return "Completed"
        elif completed_steps == 0:
            return "Not started"
        else:
            # Find the last completed step
            step_order = list(step_states.keys())
            last_completed_step = "None"
            for step in reversed(step_order):
                if step_states[step] == "COMPLETED":
                    last_completed_step = step
                    break
            return f"Last completed: {last_completed_step}"

    def get_last_run_timestamp(self, metadata):
        """Calculate last run timestamp"""
        # Check if run is currently running AND not paused
        is_running = metadata.get('isRunning', False)
        is_paused = metadata.get('isPaused', False)

        if is_running and not is_paused:
            return "Currently running"

        # Check for actual last_run_timestamp first
        last_run_timestamp = metadata.get('last_run_timestamp')
        if last_run_timestamp:
            return last_run_timestamp

        # Fallback: Check if any steps have been completed
        step_states = metadata.get('step_states', {})
        completed_steps = sum(1 for state in step_states.values() if state == "COMPLETED")

        if completed_steps > 0:
            # If steps are completed but no timestamp recorded, show creation time
            return metadata.get('creation_timestamp', 'N/A')
        else:
            return "Never run"

    def fill_empty_rows(self):
        """Ensure the table is filled with empty rows to match the table's current height."""
        total_rows = self.widgets.runsTable.rowCount()

        # Check if the row height is valid (greater than 0)
        row_height = self.widgets.runsTable.rowHeight(0)
        
        if row_height > 0:
            total_visible_rows = self.widgets.runsTable.viewport().height() // row_height
        else:
            # If row height is invalid, we assume 1 visible row as a fallback
            total_visible_rows = 1

        # If the table has fewer rows than the visible area, add empty rows to fill the space
        if total_rows < total_visible_rows:
            empty_rows_needed = total_visible_rows - total_rows
            for _ in range(empty_rows_needed):
                self.widgets.runsTable.insertRow(total_rows)  # Insert an empty row at the bottom
        elif total_rows == 0:
            # If no rows are present, add one empty row to prevent the table from being blank
            self.widgets.runsTable.insertRow(0)

    def select_run(self):
        selected_items = self.widgets.runsTable.selectedItems()
        if selected_items:
            Settings.SELECTED_RUN = selected_items[0].text()
            Settings.METADATA = Metadata(Settings.SELECTED_RUN)
            self.widgets.currentlySelected.setText(Settings.SELECTED_RUN)
            # Enable tab buttons
            self.main_window.enable_button(self.widgets.runProgressButton, lambda: self.main_window.on_menu_button_clicked(self.widgets.runProgressTab, self.widgets.runProgressButton, "runProgressButton"))
            self.main_window.enable_button(self.widgets.runConfigurationButton, lambda: self.main_window.on_menu_button_clicked(self.widgets.runConfigurationTab, self.widgets.runConfigurationButton, "runConfigurationButton"))
            self.main_window.enable_button(self.widgets.resultsOverviewButton, lambda: self.main_window.on_menu_button_clicked(self.widgets.resultsOverviewTab, self.widgets.resultsOverviewButton, "resultsOverviewButton"))
            # Enable run management buttons
            self.widgets.deleteRunButton.setEnabled(True)
            self.widgets.renameRunButton.setEnabled(True)
            self.widgets.openFolderLocationButton.setEnabled(True)
            self.widgets.exportRunButton.setEnabled(True)
            self.main_window.run_configuration.load_from_metadata()
            self.main_window.run_progress.load_from_metadata()
            self.main_window.results_overview.load_run_data()
        else:
            Settings.SELECTED_RUN = None
            Settings.METADATA = None
            self.widgets.currentlySelected.setText("None")
            # Disable tab buttons
            self.main_window.disable_button(self.widgets.runProgressButton)
            self.main_window.disable_button(self.widgets.runConfigurationButton)
            self.main_window.disable_button(self.widgets.resultsOverviewButton)
            # Disable run management buttons
            self.widgets.deleteRunButton.setEnabled(False)
            self.widgets.renameRunButton.setEnabled(False)
            self.widgets.openFolderLocationButton.setEnabled(False)
            self.widgets.exportRunButton.setEnabled(False)

    def select_specific_run(self, run):
        Settings.SELECTED_RUN = run
        self.widgets.currentlySelected.setText(run)
        if(run):
            # Enable tab buttons
            self.main_window.enable_button(self.widgets.runProgressButton, lambda: self.main_window.on_menu_button_clicked(self.widgets.runProgressTab, self.widgets.runProgressButton, "runProgressButton"))
            self.main_window.enable_button(self.widgets.runConfigurationButton, lambda: self.main_window.on_menu_button_clicked(self.widgets.runConfigurationTab, self.widgets.runConfigurationButton, "runConfigurationButton"))
            self.main_window.enable_button(self.widgets.resultsOverviewButton, lambda: self.main_window.on_menu_button_clicked(self.widgets.resultsOverviewTab, self.widgets.resultsOverviewButton, "resultsOverviewButton"))
            # Enable run management buttons
            self.widgets.deleteRunButton.setEnabled(True)
            self.widgets.renameRunButton.setEnabled(True)
            self.widgets.openFolderLocationButton.setEnabled(True)
            self.widgets.exportRunButton.setEnabled(True)
            Settings.METADATA = Metadata(Settings.SELECTED_RUN)
            self.main_window.run_configuration.load_from_metadata()
            self.main_window.run_progress.load_from_metadata()
            self.main_window.results_overview.load_run_data()
        else:
            Settings.METADATA = None
            # Disable tab buttons
            self.main_window.disable_button(self.widgets.runProgressButton)
            self.main_window.disable_button(self.widgets.runConfigurationButton)
            self.main_window.disable_button(self.widgets.resultsOverviewButton)
            # Disable run management buttons
            self.widgets.deleteRunButton.setEnabled(False)
            self.widgets.renameRunButton.setEnabled(False)
            self.widgets.openFolderLocationButton.setEnabled(False)
            self.widgets.exportRunButton.setEnabled(False)

    def create_run(self):
        button = QMessageBox.question(
            self.main_window,
            "Are you sure?",
            "Are you sure you want to create a new run?",
        )
        if button == QMessageBox.Yes:
            # Prompt user for a name for the new run directory
            run_name, ok = QInputDialog.getText(self.main_window, "New Run", "Enter a name for the new run:")

            if ok and run_name:
                # Check if the name is valid and doesn't already exist
                new_run_path = os.path.join(Settings.RUNS_DIR, run_name)

                if not os.path.exists(new_run_path):
                    # Create the new directory
                    try:
                        os.makedirs(new_run_path)

                        # Create metadata.json via Metadata class
                        metadata = Metadata(run_name)

                        self.update_runs_table()
                        self.select_specific_run(run_name)
                        # Show success message
                        QMessageBox.information(self.main_window, "Success", f"New run '{run_name}' created!")

                    except Exception as e:
                        # Handle errors during directory creation or file writing
                        QMessageBox.critical(self.main_window, "Error", f"Failed to create directory or metadata file: {e}")
                else:
                    # Notify user if the directory already exists
                    QMessageBox.warning(self.main_window, "Warning", f"A run with the name '{run_name}' already exists.")

    def delete_run(self):
        """Delete the selected run after user confirmation and cleaning up Docker containers."""
        if Settings.SELECTED_RUN is None:
            QMessageBox.warning(self.main_window, "No Selection", "No run selected to delete!")
            return

        # Confirm deletion with the user
        button = QMessageBox.critical(
            self.main_window,
            "Are you sure?",
            f"Are you sure you want to delete the run '{Settings.SELECTED_RUN}'?\n\nThis will first clean up any Docker containers associated with this run, then delete all run data.",
            buttons=QMessageBox.Yes | QMessageBox.No,
            defaultButton=QMessageBox.No,
        )

        if button == QMessageBox.Yes:
            self.run_to_delete = Settings.SELECTED_RUN
            run_path = os.path.join(Settings.RUNS_DIR, self.run_to_delete)

            if os.path.exists(run_path):
                try:
                    # First, check if the run has any Docker containers and clean them
                    metadata = Metadata(self.run_to_delete)
                    container_id = metadata.get("docker_container_id", None)

                    if container_id:
                        # Show progress dialog with cancel option
                        self.progress_dialog = QMessageBox(self.main_window)
                        self.progress_dialog.setWindowTitle("Cleaning Up Docker Container")
                        self.progress_dialog.setText(f"Cleaning up Docker container for run '{self.run_to_delete}'...\n\nThis may take a few moments.")
                        self.progress_dialog.setStandardButtons(QMessageBox.Cancel)
                        self.progress_dialog.setDefaultButton(QMessageBox.Cancel)

                        # Start async Docker cleanup
                        self._start_async_docker_cleanup(self.run_to_delete, container_id)

                        # Show the dialog non-blocking
                        result = self.progress_dialog.exec()
                        if result == QMessageBox.Cancel:
                            # User cancelled, stop the cleanup if possible
                            if hasattr(self, 'docker_cleanup_worker') and self.docker_cleanup_worker.isRunning():
                                self.docker_cleanup_worker.terminate()
                            return
                    else:
                        # No Docker container, proceed directly with file deletion
                        self._delete_run_files()

                except Exception as e:
                    QMessageBox.critical(self.main_window, "Error", f"Failed to delete the run: {e}")
            else:
                QMessageBox.warning(self.main_window, "Error", f"The run '{self.run_to_delete}' does not exist.")
        else:
            print("Deletion cancelled.")

    def _start_async_docker_cleanup(self, run_name: str, container_id: str):
        """Start asynchronous Docker container cleanup"""
        from .docker_worker import AsyncDockerWorker, DockerManager

        self.docker_cleanup_worker = AsyncDockerWorker(
            DockerManager.clean_container,
            container_id
        )
        self.docker_cleanup_worker.finished.connect(
            lambda success, error, cid: self._on_docker_cleanup_finished(success, error, cid, run_name)
        )
        self.docker_cleanup_worker.start()

    def _on_docker_cleanup_finished(self, success: bool, error: str, container_id: str, run_name: str):
        """Handle completion of Docker cleanup before proceeding with file deletion"""
        # Close the progress dialog
        if hasattr(self, 'progress_dialog'):
            self.progress_dialog.close()

        if success:
            # Update metadata to remove Docker references
            try:
                metadata = Metadata(run_name)
                metadata.delete("docker_container_id")
                metadata.delete("docker_host_port")
                metadata.delete("docker_container_owner")
                print(f"Successfully cleaned Docker container {container_id} for run {run_name}")
            except Exception as e:
                print(f"Error updating metadata after Docker cleanup: {e}")

            # Now proceed with file deletion
            self._delete_run_files()
        else:
            # Docker cleanup failed, ask user if they want to proceed anyway
            reply = QMessageBox.question(
                self.main_window,
                "Docker Cleanup Failed",
                f"Failed to clean up Docker container:\n{error}\n\nDo you want to proceed with deleting the run files anyway?",
                QMessageBox.Yes | QMessageBox.No,
                QMessageBox.No
            )
            if reply == QMessageBox.Yes:
                self._delete_run_files()

    def _delete_run_files(self):
        """Delete the run directory and files"""
        try:
            run_path = os.path.join(Settings.RUNS_DIR, self.run_to_delete)

            # Recursively delete the directory and its contents
            for root, dirs, files in os.walk(run_path, topdown=False):
                for name in files:
                    os.remove(os.path.join(root, name))  # Delete file
                for name in dirs:
                    os.rmdir(os.path.join(root, name))  # Delete empty directory

            # Remove the empty directory
            os.rmdir(run_path)

            # Update the UI
            self.update_runs_table()
            self.select_run()

            QMessageBox.information(self.main_window, "Success", f"Run '{self.run_to_delete}' has been deleted successfully.")
        except Exception as e:
            QMessageBox.critical(self.main_window, "Error", f"Failed to delete the run files: {e}")

    def import_run(self):
        """Allow the user to import one or more .zip files into the 'runs' directory."""
        # Open the file dialog for selecting multiple zip files
        files, _ = QFileDialog.getOpenFileNames(
            self.main_window,
            caption="Select one or more files to import",
            filter="*.zip"
        )
        
        if files:
            for file_path in files:
                try:
                    # Extract each zip file into the 'runs' directory
                    with zipfile2.ZipFile(file_path, 'r') as zip_ref:
                        zip_ref.extractall(Settings.RUNS_DIR)
                        print(f"Extracted {file_path} to {Settings.RUNS_DIR}")
                        
                    QMessageBox.information(self.main_window, "Success", f"Successfully imported {file_path}.")
                except Exception as e:
                    QMessageBox.critical(self.main_window, "Error", f"Failed to import {file_path}: {str(e)}")
            self.update_runs_table()
    
    def export_run(self):
        """Allow the user to export either the selected run or the entire 'runs' directory as a .zip file."""
        # Determine which folder to export based on whether a run is selected
        if Settings.SELECTED_RUN:
            # Export the selected run
            folder_to_export = os.path.join(Settings.RUNS_DIR, Settings.SELECTED_RUN)
        else:
            # Export the entire 'runs' directory
            folder_to_export = Settings.RUNS_DIR

        # Prompt the user to select where to save the zip file
        dest, _ = QFileDialog.getSaveFileName(
            self.main_window,
            caption="Select where to export to",
            filter="*.zip"
        )

        # If the user selected a destination file
        if dest:
            # Check if the file already has a '.zip' extension, and add it if not
            if not dest.lower().endswith('.zip'):
                dest += '.zip'

            try:
                # Create a new zip file at the destination path
                with zipfile2.ZipFile(dest, 'w', zipfile2.ZIP_DEFLATED) as zf:
                    # Walk through the selected folder and add files and subdirectories to the zip file
                    for root, dirs, files in os.walk(folder_to_export):
                        for file in files:
                            file_path = os.path.join(root, file)
                            # Add each file to the zip file
                            zf.write(file_path, os.path.relpath(file_path, Settings.RUNS_DIR))
                QMessageBox.information(self.main_window, "Success", f"Successfully exported to {dest}.")
            except Exception as e:
                QMessageBox.critical(self.main_window, "Error", f"Failed to export: {str(e)}")

    def open_folder_location(self):
        filepath = Settings.RUNS_DIR
        if Settings.SELECTED_RUN:
            filepath += '/' + Settings.SELECTED_RUN
        if platform.system() == 'Darwin':       # macOS
            subprocess.Popen(['open', filepath])
        elif platform.system() == 'Windows':    # Windows
            os.startfile(filepath)
        else:                                   # linux variants
            subprocess.Popen(['xdg-open', filepath])

    def rename_run(self):
        if not Settings.SELECTED_RUN:
            QMessageBox.warning(self.main_window, "Error", "No run selected!")
            return

        # Ask for new name using input dialog
        new_name, ok = QInputDialog.getText(
            self.main_window,
            "Rename Run",
            f"Enter new name for '{Settings.SELECTED_RUN}':"
        )

        if not ok or not new_name.strip():
            return  # User cancelled or empty input

        new_name = new_name.strip()
        old_path = os.path.join(Settings.RUNS_DIR, Settings.SELECTED_RUN)
        new_path = os.path.join(Settings.RUNS_DIR, new_name)

        if not os.path.exists(old_path):
            QMessageBox.critical(self.main_window, "Error", f"Run folder '{Settings.SELECTED_RUN}' does not exist.")
            return

        if os.path.exists(new_path):
            QMessageBox.critical(self.main_window, "Error", f"A folder named '{new_name}' already exists.")
            return

        try:
            os.rename(old_path, new_path)
            self.select_specific_run(new_name)
            self.update_runs_table()
            QMessageBox.information(self.main_window, "Success", f"Run renamed to '{new_name}'")
        except Exception as e:
            QMessageBox.critical(self.main_window, "Error", f"Failed to rename: {e}")

    def _zipdir(self, path, zf):
        for root, dirs, files in os.walk(path):
            for file in files:
                zf.write(
                    os.path.join(root, file),
                    os.path.relpath(os.path.join(root, file), os.path.join(path, '..'))
                )

    def on_resize(self, event):
        self.update_runs_table()
        event.accept()
