import os
import subprocess
import platform
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from . settings import Settings


class ResultsOverview:
    def __init__(self, main_window):
        self.main_window = main_window
        self.widgets = main_window.ui
        self.settings = Settings()
        self.selected_file_path = None

        self.setup_ui()

    def setup_ui(self):
        # Use the UI-defined widgets instead of creating them programmatically
        self.folder_tree = self.widgets.fileTreeWidget
        self.data_table = self.widgets.fileContentTable
        self.status_label = self.widgets.fileStatusLabel
        self.open_file_button = self.widgets.openFileButton
        self.open_directory_button = self.widgets.openDirectoryButton

        # Connect signals
        self.folder_tree.itemClicked.connect(self.on_file_selected)
        self.open_file_button.clicked.connect(self.open_selected_file)
        self.open_directory_button.clicked.connect(self.open_run_directory)

        # Configure table widget
        self.data_table.horizontalHeader().setStretchLastSection(True)

        # Initially disable the open file button
        self.open_file_button.setEnabled(False)

        # Set splitter proportions (30% left, 70% right)
        self.widgets.resultsSplitter.setSizes([300, 700])

    def load_run_data(self):
        """Load data when a run is selected"""
        if not Settings.SELECTED_RUN:
            self.status_label.setText("Select a file to view its contents")
            self.folder_tree.clear()
            self.data_table.setRowCount(0)
            self.data_table.setColumnCount(0)
            return

        run_path = os.path.join(Settings.RUNS_DIR, Settings.SELECTED_RUN)

        # Load folder structure
        self.load_folder_structure(run_path)

        # Load Excel data (first peak file)
        self.load_peak_data(run_path)

    def load_folder_structure(self, run_path):
        """Populate the folder tree with run directory contents"""
        self.folder_tree.clear()

        if not os.path.exists(run_path):
            return

        # Create root item
        root_item = QTreeWidgetItem([Settings.SELECTED_RUN])
        root_item.setData(0, Qt.UserRole, run_path)
        self.folder_tree.addTopLevelItem(root_item)

        # Recursively add items
        self.add_folder_items(root_item, run_path)

        # Expand root
        root_item.setExpanded(True)

    def add_folder_items(self, parent_item, folder_path):
        """Recursively add folder contents to tree"""
        try:
            items = os.listdir(folder_path)
            items.sort()  # Sort alphabetically

            for item_name in items:
                item_path = os.path.join(folder_path, item_name)
                tree_item = QTreeWidgetItem([item_name])
                tree_item.setData(0, Qt.UserRole, item_path)

                if os.path.isdir(item_path):
                    # Folder
                    tree_item.setIcon(0, self.main_window.style().standardIcon(QStyle.SP_DirIcon))
                    self.add_folder_items(tree_item, item_path)
                else:
                    # File
                    tree_item.setIcon(0, self.main_window.style().standardIcon(QStyle.SP_FileIcon))

                parent_item.addChild(tree_item)

        except PermissionError:
            pass  # Skip folders we can't read

    def load_peak_data(self, run_path):
        """Load the first peak Excel file data"""
        bed2peak_path = os.path.join(run_path, "bed2peak")

        if not os.path.exists(bed2peak_path):
            self.status_label.setText("No bed2peak directory found")
            self.data_table.setRowCount(0)
            self.data_table.setColumnCount(0)
            return

        # Look for the first peak text file (aligned.d0.peak.merge.txt)
        peak_file = os.path.join(bed2peak_path, "aligned.d0.peak.merge.txt")

        if not os.path.exists(peak_file):
            self.status_label.setText("No aligned.d0.peak.merge.txt file found")
            self.data_table.setRowCount(0)
            self.data_table.setColumnCount(0)
            return

        try:
            data, headers = self.read_txt_file(peak_file)

            # Set up table
            self.data_table.setRowCount(len(data))
            self.data_table.setColumnCount(len(headers))
            self.data_table.setHorizontalHeaderLabels(headers)

            # Populate table
            for row_idx, row_data in enumerate(data):
                for col_idx, value in enumerate(row_data):
                    item = QTableWidgetItem(str(value))
                    self.data_table.setItem(row_idx, col_idx, item)

            # Resize columns to content
            self.data_table.resizeColumnsToContents()

            self.status_label.setText(f"Loaded {len(data)} peaks from aligned.d0.peak.merge.txt")

        except Exception as e:
            self.status_label.setText(f"Error loading text file: {str(e)}")
            self.data_table.setRowCount(0)
            self.data_table.setColumnCount(0)

    def on_file_selected(self, item, column):
        """Handle file selection in tree"""
        file_path = item.data(0, Qt.UserRole)
        self.selected_file_path = file_path

        # Enable button only for files
        if os.path.isfile(file_path):
            self.open_file_button.setEnabled(True)
        else:
            self.open_file_button.setEnabled(False)

        if os.path.isfile(file_path) and file_path.endswith('.txt'):
            # If it's a text file, try to load it
            try:
                data, headers = self.read_txt_file(file_path)

                # Set up table
                self.data_table.setRowCount(len(data))
                self.data_table.setColumnCount(len(headers))
                self.data_table.setHorizontalHeaderLabels(headers)

                # Populate table
                for row_idx, row_data in enumerate(data):
                    for col_idx, value in enumerate(row_data):
                        item_widget = QTableWidgetItem(str(value))
                        self.data_table.setItem(row_idx, col_idx, item_widget)

                # Resize columns to content
                self.data_table.resizeColumnsToContents()

                file_name = os.path.basename(file_path)
                self.status_label.setText(f"Loaded {len(data)} rows from {file_name}")

            except Exception as e:
                self.status_label.setText(f"Error loading {os.path.basename(file_path)}: {str(e)}")
        else:
            # For other file types, clear table and show message
            file_name = os.path.basename(file_path)
            if os.path.isfile(file_path):
                # Clear the table
                self.data_table.setRowCount(0)
                self.data_table.setColumnCount(0)

                # Show message that file can't be displayed
                self.status_label.setText(f"Selected: {file_name} - This file type cannot be displayed in the table")
            else:
                # For directories, just show selection
                self.status_label.setText(f"Selected: {file_name}")

    def read_txt_file(self, file_path):
        """Read tab-delimited text file"""
        with open(file_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()

        if not lines:
            return [], []

        # Check if first line looks like data (all numeric/genomic coordinates)
        first_line = lines[0].strip().split('\t')

        # For peak files, create appropriate headers
        if file_path.endswith('peak.merge.txt'):
            headers = ['Chromosome', 'Start', 'End', 'Name', 'Score', 'Strand', 'Peak_Height']
        else:
            # Try to determine if first line is headers or data
            if any(not col.replace('.', '').replace('-', '').isdigit() for col in first_line if col):
                # First line appears to be headers
                headers = first_line
                data_lines = lines[1:]
            else:
                # First line appears to be data, create generic headers
                headers = [f'Column_{i+1}' for i in range(len(first_line))]
                data_lines = lines

        # For peak files, all lines are data
        if file_path.endswith('peak.merge.txt'):
            data_lines = lines

        # Parse data lines
        data = []
        for line in data_lines:
            row = line.strip().split('\t')
            # Pad with empty strings if row is shorter than headers
            while len(row) < len(headers):
                row.append('')
            data.append(row)

        return data, headers

    def open_selected_file(self):
        """Open the selected file in the default application"""
        if not self.selected_file_path or not os.path.isfile(self.selected_file_path):
            return

        try:
            system = platform.system()
            if system == "Windows":
                os.startfile(self.selected_file_path)
            elif system == "Darwin":  # macOS
                subprocess.Popen(["open", self.selected_file_path])
            else:  # Linux and other Unix-like systems
                subprocess.Popen(["xdg-open", self.selected_file_path])
        except Exception as e:
            # Show error message if opening fails
            from PySide6.QtWidgets import QMessageBox
            QMessageBox.warning(
                self.main_window,
                "Error",
                f"Could not open file: {str(e)}"
            )

    def open_run_directory(self):
        """Open the run directory in file explorer"""
        if not Settings.SELECTED_RUN:
            from PySide6.QtWidgets import QMessageBox
            QMessageBox.warning(
                self.main_window,
                "No Run Selected",
                "Please select a run first."
            )
            return

        filepath = os.path.join(Settings.RUNS_DIR, Settings.SELECTED_RUN)

        if not os.path.exists(filepath):
            from PySide6.QtWidgets import QMessageBox
            QMessageBox.warning(
                self.main_window,
                "Directory Not Found",
                f"Run directory '{filepath}' does not exist."
            )
            return

        try:
            system = platform.system()
            if system == "Darwin":  # macOS
                subprocess.Popen(['open', filepath])
            elif system == "Windows":  # Windows
                os.startfile(filepath)
            else:  # Linux and other Unix-like systems
                subprocess.Popen(['xdg-open', filepath])
        except Exception as e:
            from PySide6.QtWidgets import QMessageBox
            QMessageBox.warning(
                self.main_window,
                "Error",
                f"Could not open directory: {str(e)}"
            )
