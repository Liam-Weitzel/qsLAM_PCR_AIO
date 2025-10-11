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
import random
import string

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
        self.r1 = None
        self.r2 = None
        self.widgets.r1InputButton.clicked.connect(lambda: self.select_read(1))
        self.widgets.r2InputButton.clicked.connect(lambda: self.select_read(2))
        self.update_read_borders()
        self.on_configure_button_clicked(self.widgets.docker, self.widgets.dockerConfig)

        self.widgets.saveButton.clicked.connect(self.save_to_metadata)
        self.widgets.restoreDefaultsButton.clicked.connect(self.restore_defaults)
        self.widgets.resetButton.clicked.connect(self.reset)

        self.widgets.umiCheckbox.stateChanged.connect(lambda: self.on_umi_checkbox_state_changed(self.widgets.umiCheckbox.checkState()))
        self.on_umi_checkbox_state_changed(self.widgets.umiCheckbox.checkState())

        # DOCKER CONFIG SETUP
        docker_path = self.settings.get("DOCKER_PATH", "docker")
        self.widgets.dockerPathInput.setText(docker_path)
        self.widgets.remoteRadio.setChecked(True)
        self.widgets.localRadio.setChecked(False)
        self.widgets.localRadio.toggled.connect(self.update_docker_stack)
        self.widgets.remoteRadio.toggled.connect(self.update_docker_stack)
        self.widgets.checkAgainButton.clicked.connect(self.check_and_save_docker_path)
        self.widgets.usePublicServerButton.clicked.connect(self.use_public_test_server)
        self.widgets.testConnectionButton.clicked.connect(self.test_connection)
        self.update_docker_stack()
        self.check_and_save_docker_path()

    def update_read_borders(self):
        r1_style = "border: 1px solid green; border-radius: 6px;" if self.r1 else "border: 1px solid red; border-radius: 6px;"
        r2_style = "border: 1px solid green; border-radius: 6px;" if self.r2 else "border: 1px solid red; border-radius: 6px;"

        self.widgets.r1InputButton.setStyleSheet(r1_style)
        self.widgets.r2InputButton.setStyleSheet(r2_style)

    def select_read(self, num):
        file, _ = QFileDialog.getOpenFileName(
            self.main_window,
            caption=f"Select your read {num}",
            filter="*.fastq.gz"
        )
        if file:
            if num == 1:
                self.r1 = file
            elif num == 2:
                self.r2 = file
        self.update_read_borders()

    def update_docker_stack(self):
        if self.widgets.localRadio.isChecked():
            self.widgets.dockerStackedWidget.setCurrentIndex(0)
        else:
            self.widgets.dockerStackedWidget.setCurrentIndex(1)

    def check_and_save_docker_path(self):
        docker_path = self.widgets.dockerPathInput.text() or "docker"
        if self.is_docker_installed(docker_path):
            self.settings.set("DOCKER_PATH", docker_path)
            self.widgets.isInstalledStackedWidget.setCurrentIndex(0)
        else:
            self.widgets.isInstalledStackedWidget.setCurrentIndex(1)

    def test_connection(self):
        # DUMMY FUNC
        QMessageBox.information(
            self.main_window,
            "Connection Test",
            "✅ Connection works!"
        )

    def use_public_test_server(self):
        # DUMMY FUNC
        random_ip = f"192.168.{random.randint(0, 255)}.{random.randint(0, 255)}"
        random_port = str(random.randint(1024, 65535))
        random_token = ''.join(random.choices(string.ascii_letters + string.digits, k=16))

        self.widgets.ipAddressInput.setText(random_ip)
        self.widgets.portInput.setText(random_port)
        self.widgets.httpRadio.setChecked(False)
        self.widgets.httpsRadio.setChecked(True)
        self.widgets.authTokenInput.setText(random_token)

        self.widgets.remoteRadio.setChecked(True)
        self.update_docker_stack()

    def load_from_metadata(self):
        self.r1 = Settings.METADATA.get("r1", None)
        self.r2 = Settings.METADATA.get("r2", None)
        self.update_read_borders()
        umi_enabled = Settings.METADATA.get("umi_enabled", False)
        self.widgets.umiCheckbox.setCheckState(Qt.CheckState.Checked if umi_enabled else Qt.CheckState.Unchecked)

        self.widgets.umiInput.setText(Settings.METADATA.get("umi_input", ""))
        self.on_umi_checkbox_state_changed(self.widgets.umiCheckbox.checkState())

        # --- Load Docker mode ---
        docker_mode = Settings.METADATA.get("docker_mode", "remote")
        if docker_mode == "local":
            self.widgets.localRadio.setChecked(True)
        else:
            self.widgets.remoteRadio.setChecked(True)

        # --- Load Docker Path ---
        docker_path = self.settings.get("DOCKER_PATH", "docker")
        self.widgets.dockerPathInput.setText(docker_path)

        # --- Load Remote Config ---
        self.widgets.ipAddressInput.setText(Settings.METADATA.get("docker_ip", ""))
        self.widgets.portInput.setText(Settings.METADATA.get("docker_port", ""))
        self.widgets.authTokenInput.setText(Settings.METADATA.get("docker_auth_token", ""))

        protocol = Settings.METADATA.get("docker_protocol", "http")
        if protocol == "https":
            self.widgets.httpsRadio.setChecked(True)
        else:
            self.widgets.httpRadio.setChecked(True)

        # Update widgets
        self.update_docker_stack()
        self.check_and_save_docker_path()

    def save_to_metadata(self):
        Settings.METADATA.set("r1", self.r1)
        Settings.METADATA.set("r2", self.r2)
        Settings.METADATA.set("umi_enabled", self.widgets.umiCheckbox.checkState() == Qt.CheckState.Checked)
        Settings.METADATA.set("umi_input", self.widgets.umiInput.text())

        # --- Save Docker mode ---
        docker_mode = "local" if self.widgets.localRadio.isChecked() else "remote"
        Settings.METADATA.set("docker_mode", docker_mode)

        # --- Save Docker path ---
        Settings.METADATA.set("docker_path", self.widgets.dockerPathInput.text())

        # --- Save Remote Config ---
        Settings.METADATA.set("docker_ip", self.widgets.ipAddressInput.text().strip())
        Settings.METADATA.set("docker_port", self.widgets.portInput.text().strip())
        Settings.METADATA.set("docker_auth_token", self.widgets.authTokenInput.text().strip())

        protocol = "https" if self.widgets.httpsRadio.isChecked() else "http"
        Settings.METADATA.set("docker_protocol", protocol)

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
                cmd = f"{docker_path} --version"
            else:
                cmd = "docker --version"

            result = subprocess.run(
                cmd,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                shell=True  # execute the whole string in the shell
            )
            return result.returncode == 0
        except (FileNotFoundError, PermissionError, OSError, ValueError) as e:
            print(f"Docker not found or failed to run: {e}")
            return False

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
