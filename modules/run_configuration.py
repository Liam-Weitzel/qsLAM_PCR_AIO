from . settings import Settings
import xml.etree.ElementTree as ET
from PySide6.QtNetwork import QNetworkAccessManager, QNetworkRequest, QNetworkReply
import base64
import sys
import os
import subprocess
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

class RunConfiguration:
    def __init__(self, main_window):
        self.main_window = main_window
        self.widgets = main_window.ui
        self.selectedButton = None
        self.settings = Settings()

        # self.get_nc_folder_contents(main_window.network_manager, Settings.REF_RENOMES_SHARE_TOKEN)

        self.widgets.dockerConfig.clicked.connect(lambda: self.on_configure_button_clicked(self.widgets.docker, self.widgets.dockerConfig))
        self.widgets.trimmingConfig.clicked.connect(lambda: self.on_configure_button_clicked(self.widgets.trimming, self.widgets.trimmingConfig))
        self.widgets.refGenomeConfig.clicked.connect(lambda: self.on_configure_button_clicked(self.widgets.ref_genome, self.widgets.refGenomeConfig))
        self.widgets.readMappingConfig.clicked.connect(lambda: self.on_configure_button_clicked(self.widgets.read_mapping, self.widgets.readMappingConfig))
        self.widgets.siteAnalysisConfig.clicked.connect(lambda: self.on_configure_button_clicked(self.widgets.site_analysis, self.widgets.siteAnalysisConfig))
        self.on_configure_button_clicked(self.widgets.docker, self.widgets.dockerConfig)

        self.widgets.saveButton.clicked.connect(self.save_to_metadata)
        self.widgets.restoreDefaultsButton.clicked.connect(self.restore_defaults)
        self.widgets.resetButton.clicked.connect(self.reset)

        self.widgets.umiCheckbox.stateChanged.connect(lambda: self.on_umi_checkbox_state_changed(self.widgets.umiCheckbox.checkState()))
        self.on_umi_checkbox_state_changed(self.widgets.umiCheckbox.checkState())

    def load_from_metadata(self):
        self.widgets.R1Input.setText(Settings.METADATA.get("r1", ""))
        self.widgets.R2Input.setText(Settings.METADATA.get("r2", ""))
        
        umi_enabled = Settings.METADATA.get("umi_enabled", False)
        self.widgets.umiCheckbox.setCheckState(Qt.CheckState.Checked if umi_enabled else Qt.CheckState.Unchecked)

        self.widgets.umiInput.setText(Settings.METADATA.get("umi_input", ""))
        self.on_umi_checkbox_state_changed(self.widgets.umiCheckbox.checkState())

    def save_to_metadata(self):
        Settings.METADATA.set("r1", self.widgets.R1Input.text())
        Settings.METADATA.set("r2", self.widgets.R2Input.text())
        Settings.METADATA.set("umi_enabled", self.widgets.umiCheckbox.checkState() == Qt.CheckState.Checked)
        Settings.METADATA.set("umi_input", self.widgets.umiInput.text())

    def on_configure_button_clicked(self, page, button):
        if(self.selectedButton == button): return
        self.widgets.configStackedWidget.setCurrentWidget(page)
        current_style = button.styleSheet()
        if "background-color: lightblue;" not in current_style:
            current_style += " background-color: lightblue;"
        button.setStyleSheet(current_style)

        if(self.selectedButton):
            current_style = self.selectedButton.styleSheet()
            if "background-color: lightblue;" in current_style:
                current_style = current_style.replace(" background-color: lightblue;", "")
            self.selectedButton.setStyleSheet(current_style)

        self.selectedButton = button

    def is_docker_installed(self, docker_path) -> bool:
        try:
            if docker_path and isinstance(docker_path, str) and docker_path.strip():
                cmd = [docker_path.strip(), "--version"]
            else:
                cmd = ["docker", "--version"]

            result = subprocess.run(
                cmd,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True  # ensures output is str, not bytes
            )
            return result.returncode == 0
        except (FileNotFoundError, PermissionError, OSError, ValueError) as e:
            print(f"Docker not found or failed to run: {e}")
            return False

    # def docker_not_installed(self):
    #     docker_path = self.settings.get("DOCKER_PATH", "docker")
    #
    #     if self.is_docker_installed(docker_path):
    #         self.settings.set("DOCKER_PATH", docker_path)
    #         return
    #
    #     def check_again():
    #         custom_path = docker_path_input.text().strip()
    #         if self.is_docker_installed(custom_path):
    #             self.settings.set("DOCKER_PATH", custom_path)

    def reset(self):
        """Reset the selected run to what is saved in metadata.json"""

        button = QMessageBox.critical(
            self.main_window,
            "Are you sure?",
            f"Are you sure you want to reset run '{Settings.SELECTED_RUN}' to its previously saved version?",
            buttons=QMessageBox.Yes | QMessageBox.No,
            defaultButton=QMessageBox.No,
        )

        if button == QMessageBox.Yes:
            self.load_from_metadata()

    def restore_defaults(self):
        """Restore the selected run to defaults after user confirmation."""

        button = QMessageBox.critical(
            self.main_window,
            "Are you sure?",
            f"Are you sure you want to restore run '{Settings.SELECTED_RUN}' to defaults?",
            buttons=QMessageBox.Yes | QMessageBox.No,
            defaultButton=QMessageBox.No,
        )

        if button == QMessageBox.Yes:
            self.widgets.R1Input.clear()
            self.widgets.R2Input.clear()
            self.widgets.umiCheckbox.setCheckState(Qt.CheckState.Unchecked)
            self.widgets.umiInput.clear()
            self.on_umi_checkbox_state_changed(self.widgets.umiCheckbox.checkState())
            self.save_to_metadata()

    def on_umi_checkbox_state_changed(self, state):
        if state == Qt.CheckState.Checked:
            self.widgets.umiInput.show()
        else:
            self.widgets.umiInput.hide()

    def get_nc_folder_contents(self, manager: QNetworkAccessManager, share_token: str):
        base_url = "https://nc.liam-w.com"
        webdav_url = f"{base_url}/public.php/webdav/"

        propfind_body = b'''<?xml version="1.0"?>
    <d:propfind xmlns:d="DAV:">
        <d:allprop/>
    </d:propfind>'''

        request = QNetworkRequest(QUrl(webdav_url))
        request.setHeader(QNetworkRequest.ContentTypeHeader, "application/xml")
        request.setRawHeader(b"Depth", b"1")

        auth_header = base64.b64encode(f"{share_token}:".encode()).decode()
        request.setRawHeader(b"Authorization", f"Basic {auth_header}".encode())

        # Keep a reference so it doesn't get GC'd
        self._current_reply = manager.sendCustomRequest(request, b"PROPFIND", propfind_body)

        @Slot()
        def handle_reply():
            reply = self._current_reply
            if reply.error() != QNetworkReply.NoError:
                print("Error:", reply.errorString())
                return

            data = reply.readAll().data()
            ns = {'d': 'DAV:'}
            root = ET.fromstring(data)

            files = [
                resp.find('d:href', ns).text.rstrip('/').split('/')[-1]
                for resp in root.findall('d:response', ns)[1:]  # skip folder itself
            ]

            file_download_urls = [
                f"{base_url}/s/{share_token}/download?path=%2F&files={f}"
                for f in files
            ]

            print("Files in share:", files)
            for url in file_download_urls:
                print("Download URL:", url)

            # Release reference
            self._current_reply = None

        self._current_reply.finished.connect(handle_reply)
