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

from widgets.custom_context_menu.custom_context_menu import CustomContextMenu

class RunConfiguration:
    def __init__(self, main_window):
        self.main_window = main_window
        self.widgets = main_window.ui
        self.selectedButton = None
        self.settings = Settings()

        self.reference_genomes = {}
        self.populate_reference_genome_combo_box(main_window.network_manager, Settings.REF_RENOMES_SHARE_TOKEN)

        self.widgets.dockerConfig.clicked.connect(lambda: self.on_configure_button_clicked(self.widgets.docker, self.widgets.dockerConfig))
        self.widgets.trimmingConfig.clicked.connect(lambda: self.on_configure_button_clicked(self.widgets.trimming, self.widgets.trimmingConfig))
        self.widgets.readMappingConfig.clicked.connect(lambda: self.on_configure_button_clicked(self.widgets.read_mapping, self.widgets.readMappingConfig))
        self.widgets.siteAnalysisConfig.clicked.connect(lambda: self.on_configure_button_clicked(self.widgets.site_analysis, self.widgets.siteAnalysisConfig))
        self.on_configure_button_clicked(self.widgets.docker, self.widgets.dockerConfig)
        self.widgets.r1Input.setReadOnly(True)
        self.widgets.r2Input.setReadOnly(True)
        CustomContextMenu(self.widgets.r1Input)
        CustomContextMenu(self.widgets.r2Input)
        self.widgets.r1InputButton.clicked.connect(lambda: self.select_read(1))
        self.widgets.r2InputButton.clicked.connect(lambda: self.select_read(2))

        self.widgets.saveButton.clicked.connect(self.save_to_metadata)
        self.widgets.restoreDefaultsButton.clicked.connect(self.restore_defaults)
        self.widgets.resetButton.clicked.connect(self.reset)

        self.widgets.umiCheckbox.stateChanged.connect(lambda: self.on_umi_checkbox_state_changed(self.widgets.umiCheckbox.checkState()))
        self.on_umi_checkbox_state_changed(self.widgets.umiCheckbox.checkState())

        # DOCKER CONFIG SETUP
        docker_path = self.settings.get("DOCKER_PATH", "docker")
        self.widgets.dockerPathInput.setText(docker_path)
        self.widgets.dockerPathInput_2.setText(docker_path)
        self.widgets.remoteRadio.setChecked(True)
        self.widgets.localRadio.setChecked(False)
        self.widgets.localRadio.toggled.connect(self.update_docker_stack)
        self.widgets.remoteRadio.toggled.connect(self.update_docker_stack)
        self.widgets.checkAgainButton.clicked.connect(self.check_and_save_docker_path)
        self.widgets.checkAgainButton_2.clicked.connect(self.check_and_save_docker_path)
        self.widgets.usePublicServerButton.clicked.connect(self.use_public_test_server)
        self.widgets.testConnectionButton.clicked.connect(self.test_connection)
        self.check_and_save_docker_path()

        # Connect sliders to live update labels
        self.widgets.r1ErrorRateSlider.valueChanged.connect(self.update_error_rate_labels)
        self.widgets.r2ErrorRateSlider.valueChanged.connect(self.update_error_rate_labels)

        # Initialize with current values
        self.update_error_rate_labels()

    def update_error_rate_labels(self):
        r1_value = self.widgets.r1ErrorRateSlider.value() / 100
        r2_value = self.widgets.r2ErrorRateSlider.value() / 100
        self.widgets.r1ErrorRateValueLabel.setText(f" {r1_value:.2f}")
        self.widgets.r2ErrorRateValueLabel.setText(f" {r2_value:.2f}")

    def select_read(self, num):
        file, _ = QFileDialog.getOpenFileName(
            self.main_window,
            caption=f"Select your read {num}",
            filter="*.fastq.gz"
        )
        if file:
            if num == 1:
                self.widgets.r1Input.setText(file)
            elif num == 2:
                self.widgets.r2Input.setText(file)

    def update_docker_stack(self):
        if self.widgets.localRadio.isChecked():
            self.widgets.dockerStackedWidget.setCurrentIndex(0)
        else:
            self.widgets.dockerStackedWidget.setCurrentIndex(1)

    def check_and_save_docker_path(self):
        if(self.widgets.isInstalledStackedWidget.currentIndex() == 1):
            docker_path = self.widgets.dockerPathInput.text() or "docker"
        else:
            docker_path = self.widgets.dockerPathInput_2.text() or "docker"

        if self.is_docker_installed(docker_path):
            self.settings.set("DOCKER_PATH", docker_path)
            self.main_window.run_progress.load_from_metadata()
            self.widgets.isInstalledStackedWidget.setCurrentIndex(0)
        else:
            self.widgets.isInstalledStackedWidget.setCurrentIndex(1)
        docker_path = self.settings.get("DOCKER_PATH", "docker")
        self.widgets.dockerPathInput.setText(docker_path)
        self.widgets.dockerPathInput_2.setText(docker_path)

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
        # --- GENERAL ---
        self.widgets.r1Input.setText(Settings.METADATA.get("r1", ""))
        self.widgets.r2Input.setText(Settings.METADATA.get("r2", ""))
        umi_enabled = Settings.METADATA.get("umi_enabled", False)
        self.widgets.umiCheckbox.setCheckState(Qt.CheckState.Checked if umi_enabled else Qt.CheckState.Unchecked)
        self.widgets.umiInput.setText(Settings.METADATA.get("umi_input", ""))
        self.on_umi_checkbox_state_changed(self.widgets.umiCheckbox.checkState())

        # --- DOCKER ---
        docker_mode = Settings.METADATA.get("docker_mode", "remote")
        if docker_mode == "local":
            self.widgets.localRadio.setChecked(True)
        else:
            self.widgets.remoteRadio.setChecked(True)

        docker_path = self.settings.get("DOCKER_PATH", "docker")
        self.widgets.dockerPathInput.setText(docker_path)
        self.widgets.dockerPathInput_2.setText(docker_path)

        self.widgets.ipAddressInput.setText(Settings.METADATA.get("docker_ip", ""))
        self.widgets.portInput.setText(Settings.METADATA.get("docker_port", ""))
        self.widgets.authTokenInput.setText(Settings.METADATA.get("docker_auth_token", ""))

        protocol = Settings.METADATA.get("docker_protocol", "http")
        if protocol == "https":
            self.widgets.httpsRadio.setChecked(True)
        else:
            self.widgets.httpRadio.setChecked(True)

        # --- CUTADAPT ---
        self.widgets.useCutadaptCheckbox.setChecked(Settings.METADATA.get("cutadapt_use", True))
        self.widgets.r1SequenceInput.setText(Settings.METADATA.get("cutadapt_r1_sequence", ""))
        self.widgets.r1ErrorRateSlider.setValue(int(Settings.METADATA.get("cutadapt_r1_error_rate", "30")))
        self.widgets.r1TrimLeadingInput.setText(Settings.METADATA.get("cutadapt_r1_trim_leading", "0"))
        self.widgets.r1MinOverlapInput.setText(Settings.METADATA.get("cutadapt_r1_min_overlap", "5"))
        self.widgets.r1AnchoredCheckbox.setChecked(Settings.METADATA.get("cutadapt_r1_anchored", False))
        self.widgets.r1MinLengthInput.setText(Settings.METADATA.get("cutadapt_r1_min_length", "30"))
        self.widgets.r1PairFilterComboBox.setCurrentIndex(Settings.METADATA.get("cutadapt_r1_pair_filter", 0))

        self.widgets.r2SequenceInput.setText(Settings.METADATA.get("cutadapt_r2_sequence", ""))
        self.widgets.r2ErrorRateSlider.setValue(int(Settings.METADATA.get("cutadapt_r2_error_rate", "10")))
        self.widgets.r2TrimLeadingInput.setText(Settings.METADATA.get("cutadapt_r2_trim_leading", "0"))
        self.widgets.r2MinOverlapInput.setText(Settings.METADATA.get("cutadapt_r2_min_overlap", "10"))
        self.widgets.r2AnchoredCheckbox.setChecked(Settings.METADATA.get("cutadapt_r2_anchored", False))
        self.widgets.r2MinLengthInput.setText(Settings.METADATA.get("cutadapt_r2_min_length", "30"))
        self.widgets.r2PairFilterComboBox.setCurrentIndex(Settings.METADATA.get("cutadapt_r2_pair_filter", 0))

        # --- TRIMMING ---
        self.widgets.qcAfterCheckbox.setChecked(Settings.METADATA.get("qc_after", True))
        self.widgets.qcBeforeCheckbox.setChecked(Settings.METADATA.get("qc_before", True))
        self.widgets.readLenCheckbox.setChecked(Settings.METADATA.get("read_len", True))

        # --- REFERENCE_GENOMES ---
        self.widgets.referenceGenomeComboBox.setCurrentText(Settings.METADATA.get("reference_genome", ""))

        # --- FINAL UPDATES ---
        self.update_docker_stack()
        self.check_and_save_docker_path()

    def save_to_metadata(self):
        # --- GENERAL ---
        Settings.METADATA.set("r1", self.widgets.r1Input.text())
        Settings.METADATA.set("r2", self.widgets.r2Input.text())
        Settings.METADATA.set("umi_enabled", self.widgets.umiCheckbox.checkState() == Qt.CheckState.Checked)
        Settings.METADATA.set("umi_input", self.widgets.umiInput.text())

        # --- DOCKER ---
        docker_mode = "local" if self.widgets.localRadio.isChecked() else "remote"
        Settings.METADATA.set("docker_mode", docker_mode)
        Settings.METADATA.set("docker_ip", self.widgets.ipAddressInput.text().strip())
        Settings.METADATA.set("docker_port", self.widgets.portInput.text().strip())
        Settings.METADATA.set("docker_auth_token", self.widgets.authTokenInput.text().strip())
        protocol = "https" if self.widgets.httpsRadio.isChecked() else "http"
        Settings.METADATA.set("docker_protocol", protocol)

        # --- CUTADAPT ---
        Settings.METADATA.set("cutadapt_use", self.widgets.useCutadaptCheckbox.isChecked())
        Settings.METADATA.set("cutadapt_r1_sequence", self.widgets.r1SequenceInput.text())
        Settings.METADATA.set("cutadapt_r1_error_rate", self.widgets.r1ErrorRateSlider.value())
        Settings.METADATA.set("cutadapt_r1_trim_leading", self.widgets.r1TrimLeadingInput.text())
        Settings.METADATA.set("cutadapt_r1_min_overlap", self.widgets.r1MinOverlapInput.text())
        Settings.METADATA.set("cutadapt_r1_anchored", self.widgets.r1AnchoredCheckbox.isChecked())
        Settings.METADATA.set("cutadapt_r1_min_length", self.widgets.r1MinLengthInput.text())
        Settings.METADATA.set("cutadapt_r1_pair_filter", self.widgets.r1PairFilterComboBox.currentIndex())
        Settings.METADATA.set("cutadapt_r2_sequence", self.widgets.r2SequenceInput.text())
        Settings.METADATA.set("cutadapt_r2_error_rate", self.widgets.r2ErrorRateSlider.value())
        Settings.METADATA.set("cutadapt_r2_trim_leading", self.widgets.r2TrimLeadingInput.text())
        Settings.METADATA.set("cutadapt_r2_min_overlap", self.widgets.r2MinOverlapInput.text())
        Settings.METADATA.set("cutadapt_r2_anchored", self.widgets.r2AnchoredCheckbox.isChecked())
        Settings.METADATA.set("cutadapt_r2_min_length", self.widgets.r2MinLengthInput.text())
        Settings.METADATA.set("cutadapt_r2_pair_filter", self.widgets.r2PairFilterComboBox.currentIndex())

        # --- TRIMMING ---
        Settings.METADATA.set("qc_after", self.widgets.qcAfterCheckbox.isChecked())
        Settings.METADATA.set("qc_before", self.widgets.qcBeforeCheckbox.isChecked())
        Settings.METADATA.set("read_len", self.widgets.readLenCheckbox.isChecked())

        # --- REFERENCE_GENOMES ---
        Settings.METADATA.set("reference_genome", self.widgets.referenceGenomeComboBox.currentText())
        Settings.METADATA.set("reference_genome_url", self.reference_genomes[self.widgets.referenceGenomeComboBox.currentText()])

        # --- UPDATE PROGRESS TAB ---
        # Refresh the run progress tab to reflect configuration changes immediately
        self.main_window.run_progress.load_from_metadata()

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
            # --- GENERAL ---
            self.widgets.umiCheckbox.setCheckState(Qt.CheckState.Unchecked)
            self.widgets.umiInput.clear()
            self.widgets.r1Input.clear()
            self.widgets.r2Input.clear()

            # --- DOCKER ---
            self.widgets.localRadio.setChecked(False)
            self.widgets.remoteRadio.setChecked(True)
            self.widgets.ipAddressInput.clear()
            self.widgets.portInput.clear()
            self.widgets.authTokenInput.clear()
            self.widgets.httpRadio.setChecked(True)
            self.widgets.httpsRadio.setChecked(False)

            # --- CUTADAPT (defaults from load_from_metadata) ---
            self.widgets.useCutadaptCheckbox.setChecked(True)
            self.widgets.r1SequenceInput.clear()
            self.widgets.r1ErrorRateSlider.setValue(30)
            self.widgets.r1TrimLeadingInput.setText("0")
            self.widgets.r1MinOverlapInput.setText("5")
            self.widgets.r1AnchoredCheckbox.setChecked(False)
            self.widgets.r1MinLengthInput.setText("30")
            self.widgets.r1PairFilterComboBox.setCurrentIndex(0)

            self.widgets.r2SequenceInput.clear()
            self.widgets.r2ErrorRateSlider.setValue(10)
            self.widgets.r2TrimLeadingInput.setText("0")
            self.widgets.r2MinOverlapInput.setText("10")
            self.widgets.r2AnchoredCheckbox.setChecked(False)
            self.widgets.r2MinLengthInput.setText("30")
            self.widgets.r2PairFilterComboBox.setCurrentIndex(0)

            # --- TRIMMING ---
            self.widgets.qcAfterCheckbox.setChecked(True)
            self.widgets.qcBeforeCheckbox.setChecked(True)
            self.widgets.readLenCheckbox.setChecked(True)

            # --- REFERENCE_GENOMES ---
            self.widgets.referenceGenomeComboBox.setCurrentIndex(0)

            # --- Update dependent logic ---
            self.on_umi_checkbox_state_changed(self.widgets.umiCheckbox.checkState())

            # --- Save state ---
            self.save_to_metadata()

    def on_umi_checkbox_state_changed(self, state):
        if state == Qt.CheckState.Checked:
            self.widgets.umiInput.show()
            self.widgets.trimmingTabs.setTabEnabled(2, True)
        else:
            self.widgets.umiInput.hide()
            self.widgets.trimmingTabs.setTabEnabled(2, False)

    def populate_reference_genome_combo_box(self, manager: QNetworkAccessManager, share_token: str):
        def strip_all_extensions(filename: str) -> str:
            name = filename
            while True:
                name, ext = os.path.splitext(name)
                if not ext:
                    break
            return name

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
                for resp in root.findall('d:response', ns)[1:]
            ]

            file_download_urls = [
                f"{base_url}/s/{share_token}/download?path=%2F&files={f}"
                for f in files
            ]

            # Strip extensions and build mapping: {name_without_ext: url}
            for filename, url in zip(files, file_download_urls):
                clean_name = strip_all_extensions(filename)
                self.reference_genomes[clean_name] = url

            # Save using self.settings
            self.settings.set("REFERENCE_GENOMES", self.reference_genomes)

            # Populate combo box
            combo = self.widgets.referenceGenomeComboBox
            combo.clear()
            for name, url in self.reference_genomes.items():
                combo.addItem(name, userData=url)

            if combo.count() > 0:
                combo.setCurrentIndex(0)

            self._current_reply = None

        self._current_reply.finished.connect(handle_reply)
