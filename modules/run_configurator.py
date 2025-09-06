from . settings import Settings
from PySide6.QtWidgets import QFileDialog, QMessageBox, QTableWidgetItem
from PySide6.QtCore import QTimer, Qt

class RunConfigurator:
    def __init__(self, main_window):
        self.settings = Settings()
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

        self.widgets.umiCheckbox.stateChanged.connect(lambda: self.on_umi_checkbox_state_changed(self.widgets.umiCheckbox.checkState()))
        self.on_umi_checkbox_state_changed(self.widgets.umiCheckbox.checkState())

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

    def on_umi_checkbox_state_changed(self, state):
        if state == Qt.CheckState.Checked:
            self.widgets.umiInput.show()
        else:
            self.widgets.umiInput.hide()
