from . settings import Settings
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QMessageBox

class RunConfiguration:
    def __init__(self, main_window):
        self.main_window = main_window
        self.widgets = main_window.ui
        self.selectedButton = None

        self.widgets.dockerConfig.clicked.connect(lambda: self.on_configure_button_clicked(self.widgets.docker, self.widgets.dockerConfig))
        self.widgets.trimmingConfig.clicked.connect(lambda: self.on_configure_button_clicked(self.widgets.trimming, self.widgets.trimmingConfig))
        self.widgets.step3Button.clicked.connect(lambda: self.on_configure_button_clicked(self.widgets.page_3, self.widgets.step3Button))
        self.widgets.step4Button.clicked.connect(lambda: self.on_configure_button_clicked(self.widgets.page_4, self.widgets.step4Button))
        self.widgets.step5Button.clicked.connect(lambda: self.on_configure_button_clicked(self.widgets.page_5, self.widgets.step5Button))
        self.widgets.step6Button.clicked.connect(lambda: self.on_configure_button_clicked(self.widgets.page_6, self.widgets.step6Button))
        self.on_configure_button_clicked(self.widgets.docker, self.widgets.dockerConfig)

        self.widgets.saveButton.clicked.connect(self.save_to_metadata)
        self.widgets.restoreDefaultsButton.clicked.connect(self.restore_defaults)
        self.widgets.resetButton.clicked.connect(self.reset)

        self.widgets.umiCheckbox.stateChanged.connect(lambda: self.on_umi_checkbox_state_changed(self.widgets.umiCheckbox.checkState()))
        self.on_umi_checkbox_state_changed(self.widgets.umiCheckbox.checkState())

    def load_from_metadata(self):
        self.widgets.adapterSequenceInput.setText(Settings.METADATA.get("adapter_sequence", ""))
        self.widgets.ltrPrimerSequenceInput.setText(Settings.METADATA.get("ltr_primer_sequence", ""))
        
        umi_enabled = Settings.METADATA.get("umi_enabled", False)
        self.widgets.umiCheckbox.setCheckState(Qt.CheckState.Checked if umi_enabled else Qt.CheckState.Unchecked)

        self.widgets.umiInput.setText(Settings.METADATA.get("umi_input", ""))
        self.on_umi_checkbox_state_changed(self.widgets.umiCheckbox.checkState())

    def save_to_metadata(self):
        Settings.METADATA.set("adapter_sequence", self.widgets.adapterSequenceInput.text())
        Settings.METADATA.set("ltr_primer_sequence", self.widgets.ltrPrimerSequenceInput.text())
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
            self.widgets.adapterSequenceInput.clear()
            self.widgets.ltrPrimerSequenceInput.clear()
            self.widgets.umiCheckbox.setCheckState(Qt.CheckState.Unchecked)
            self.widgets.umiInput.clear()
            self.on_umi_checkbox_state_changed(self.widgets.umiCheckbox.checkState())
            self.save_to_metadata()

    def on_umi_checkbox_state_changed(self, state):
        if state == Qt.CheckState.Checked:
            self.widgets.umiInput.show()
        else:
            self.widgets.umiInput.hide()
