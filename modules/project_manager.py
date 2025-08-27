import os
import sys
import subprocess
import zipfile2
from PySide6.QtWidgets import QFileDialog, QMessageBox
from . ui_functions import *

class ProjectManager:
    def __init__(self, main_window):
        self.main_window = main_window
        self.widgets = main_window.ui

        self.widgets.createRunButton.clicked.connect(self.create_run)
        self.widgets.deleteRunButton.clicked.connect(self.delete_run)
        self.widgets.exportRunButton.clicked.connect(self.export_run)
        self.widgets.importRunButton.clicked.connect(self.import_run)
        self.widgets.openFolderLocationButton.clicked.connect(self.open_folder_location)

        # SET FIRST LOAD PAGE AND SELECT MENU
        # ///////////////////////////////////////////////////////////////
        self.widgets.stackedWidget.setCurrentWidget(self.widgets.projectManager)
        self.widgets.projectManagerButton.setStyleSheet(UIFunctions.selectMenu(self.widgets.projectManagerButton.styleSheet()))

    def create_run(self):
        button = QMessageBox.question(
            self.main_window,
            "Are you sure?",
            "Are you sure you want to create a new run?",
        )
        print("Yes!" if button == QMessageBox.Yes else "No!")

    def delete_run(self):
        button = QMessageBox.critical(
            self.main_window,
            "Are you sure?",
            "Are you sure you want to delete run X?",
            buttons=QMessageBox.Yes | QMessageBox.No,
            defaultButton=QMessageBox.No,
        )
        print("Yes!" if button == QMessageBox.Yes else "No!")

    def import_run(self):
        files, _ = QFileDialog.getOpenFileNames(
            caption="Select one or more files to import", filter="*.zip"
        )
        for file_path in files:
            with zipfile2.ZipFile(file_path, 'r') as zip_ref:
                zip_ref.extractall("./widgets")

    def export_run(self):
        dest, _ = QFileDialog.getSaveFileName(caption="Select where to export to")
        if dest:
            with zipfile2.ZipFile(dest, 'w', zipfile2.ZIP_DEFLATED) as zf:
                self._zipdir('./images/', zf)

    def open_folder_location(self):
        if os.name == 'nt':
            os.startfile(".")
        else:
            subprocess.call(["open" if sys.platform == "darwin" else "xdg-open", "."])

    def _zipdir(self, path, zf):
        for root, dirs, files in os.walk(path):
            for file in files:
                zf.write(
                    os.path.join(root, file),
                    os.path.relpath(os.path.join(root, file), os.path.join(path, '..'))
                )
