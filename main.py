
#
# BY: WANDERSON M.PIMENTA
# PROJECT MADE WITH: Qt Designer and PySide6
# V: 1.0.0
#
# This project can be used freely for all uses, as long as they maintain the
# respective credits only in the Python scripts, any information in the visual
# interface (GUI) can be modified without any implication.
#
# There are limitations on Qt licenses if you want to use your products
# commercially, I recommend reading them on the official website:
# https://doc.qt.io/qtforpython/licenses.html
#
# ///////////////////////////////////////////////////////////////

import sys
import os

# IMPORT / GUI AND MODULES AND WIDGETS
# ///////////////////////////////////////////////////////////////
from modules import *
from widgets import *
os.environ["QT_FONT_DPI"] = "96" # FIX Problem for High DPI and Scale above 100%

# SET AS GLOBAL WIDGETS
# ///////////////////////////////////////////////////////////////
widgets = None

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # SET AS GLOBAL WIDGETS
        # ///////////////////////////////////////////////////////////////
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        global widgets
        widgets = self.ui
        self.settings = Settings()

        # APP NAME
        # ///////////////////////////////////////////////////////////////
        self.setWindowTitle(Settings.TITLE)

        # TOGGLE MENU
        # ///////////////////////////////////////////////////////////////
        widgets.toggleButton.clicked.connect(lambda: UIFunctions.toggleMenu(self, True))

        # SET UI DEFINITIONS
        # ///////////////////////////////////////////////////////////////
        UIFunctions.uiDefinitions(self)

        self.project_manager = ProjectManager(self)

        # BUTTONS CLICK - CONNECT EACH TO ITS OWN HANDLER
        # ///////////////////////////////////////////////////////////////

        # LEFT MENUS
        widgets.setupViewButton.clicked.connect(self.on_setup_view)
        widgets.runViewButton.clicked.connect(self.on_run_view)
        widgets.analysisViewButton.clicked.connect(self.on_analysis_view)
        widgets.projectManagerButton.clicked.connect(self.on_project_manager_view)

        # EXTRA LEFT BOX
        widgets.toggleLeftBox.clicked.connect(lambda: UIFunctions.toggleLeftBox(self, True))
        widgets.extraCloseColumnButton.clicked.connect(lambda: UIFunctions.toggleLeftBox(self, True))

        # EXTRA RIGHT BOX
        widgets.settingsTopButton.clicked.connect(lambda: UIFunctions.toggleRightBox(self, True))

        # SHOW APP
        # ///////////////////////////////////////////////////////////////
        self.show()
        self.show_first_time_dialog()
        self.show_docker_not_installed_dialog()

    # INDIVIDUAL HANDLERS FOR LEFT MENU BUTTONS
    # ///////////////////////////////////////////////////////////////
    def on_project_manager_view(self):
        widgets.stackedWidget.setCurrentWidget(widgets.projectManager)
        UIFunctions.resetStyle(self, "projectManagerButton")
        widgets.projectManagerButton.setStyleSheet(UIFunctions.selectMenu(widgets.projectManagerButton.styleSheet()))

    def on_setup_view(self):
        widgets.stackedWidget.setCurrentWidget(widgets.setupView)
        UIFunctions.resetStyle(self, "setupViewButton")
        widgets.setupViewButton.setStyleSheet(UIFunctions.selectMenu(widgets.setupViewButton.styleSheet()))

    def on_run_view(self):
        widgets.stackedWidget.setCurrentWidget(widgets.runView)
        UIFunctions.resetStyle(self, "runViewButton")
        widgets.runViewButton.setStyleSheet(UIFunctions.selectMenu(widgets.runViewButton.styleSheet()))

    def on_analysis_view(self):
        widgets.stackedWidget.setCurrentWidget(widgets.analysisView)
        UIFunctions.resetStyle(self, "analysisViewButton")
        widgets.analysisViewButton.setStyleSheet(UIFunctions.selectMenu(widgets.analysisViewButton.styleSheet()))

    # RESIZE EVENTS
    # ///////////////////////////////////////////////////////////////
    def resizeEvent(self, event):
        # Update Size Grips
        UIFunctions.resize_grips(self)

    # MOUSE CLICK EVENTS
    # ///////////////////////////////////////////////////////////////
    def mousePressEvent(self, event):
        # SET DRAG POS WINDOW
        self.dragPos = event.globalPosition().toPoint()

    # PRE START POPUPS
    # ///////////////////////////////////////////////////////////////
    def show_first_time_dialog(self):
        if self.settings.get("FIRST_START"):
            self.settings.set("FIRST_START", False)

            dlg = QDialog(self)
            dlg.setWindowTitle("Welcome to qsLAM_PCR_AIO")
            dlg.setMinimumWidth(400)

            layout = QVBoxLayout()

            text = QLabel(
                "Welcome to <b>qsLAM_PCR_AIO</b><br><br>"
                "This tool provides an end-to-end pipeline for analyzing integration sites using LAM-PCR data. "
                "From raw reads to annotated integration profiles, qsLAM_PCR_AIO helps researchers visualize, "
                "filter, and export results — all in one interface."
            )
            text.setWordWrap(True)
            layout.addWidget(text)

            doc_link = QTextBrowser()
            doc_link.setHtml('<a href="https://your.documentation.link" style="color: #007acc;">Visit the documentation</a><br><br><a href="https://your.documentation.link" style="color: #007acc;">Watch a guide</a>')
            doc_link.setOpenExternalLinks(True)
            layout.addWidget(doc_link)

            ok_button = QPushButton("Get Started")
            ok_button.clicked.connect(dlg.accept)
            layout.addWidget(ok_button)

            dlg.setLayout(layout)
            dlg.exec()
    
    def is_docker_installed(self, docker_path: str = None) -> bool:
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

    def show_docker_not_installed_dialog(self):
        if self.settings.get("HIDE_DOCKER_WARNING", False):
            return

        docker_path = self.settings.get("DOCKER_PATH", None)

        if self.is_docker_installed(docker_path):
            return

        # === Show dialog ===
        dlg = QDialog(self)
        dlg.setWindowTitle("Docker Not Found")
        dlg.setMinimumWidth(500)

        layout = QVBoxLayout()

        msg = QLabel(
            "🚫 <b>Docker not installed</b><br><br>"
            "I couldn't find a working Docker installation on your system. Docker is required to run the LAM-PCR pipeline locally. "
            "You can still browse the app, but the local run option will be hidden in the run configurations (second tab)."
        )
        msg.setWordWrap(True)
        layout.addWidget(msg)

        docker_link = QTextBrowser()
        docker_link.setHtml('<a href="https://www.docker.com/products/docker-desktop/" style="color: #007acc;">Install Docker</a>')
        docker_link.setOpenExternalLinks(True)
        layout.addWidget(docker_link)

        msg2 = QLabel("Think Docker is installed somewhere else? Let me know where it is:")
        layout.addWidget(msg2)

        docker_path_input = QLineEdit()
        docker_path_input.setPlaceholderText("/usr/local/bin/docker or C:\\Program Files\\Docker\\Docker\\resources\\bin\\docker.exe")
        if isinstance(docker_path, str):
            docker_path_input.setText(docker_path)
        layout.addWidget(docker_path_input)

        checkbox = QCheckBox("Don't show this warning again")
        layout.addWidget(checkbox)

        # Buttons
        button_layout = QHBoxLayout()
        check_again_button = QPushButton("Check Again")
        close_button = QPushButton("Close")

        def save_settings_and_close():
            if checkbox.isChecked():
                self.settings.set("HIDE_DOCKER_WARNING", True)

            custom_path = docker_path_input.text().strip()
            if custom_path:
                self.settings.set("DOCKER_PATH", custom_path)

            dlg.accept()

        def check_again():
            custom_path = docker_path_input.text().strip()
            if self.is_docker_installed(custom_path):
                self.settings.set("DOCKER_PATH", custom_path)
                dlg.accept()  # Docker found, dismiss dialog
            else:
                docker_path_input.setStyleSheet("border: 1px solid red;")
                docker_path_input.setPlaceholderText("🚫 Docker not found at that path")

        check_again_button.clicked.connect(check_again)
        close_button.clicked.connect(save_settings_and_close)

        button_layout.addWidget(check_again_button)
        button_layout.addWidget(close_button)
        layout.addLayout(button_layout)

        dlg.setLayout(layout)
        dlg.exec()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("icon.ico"))
    window = MainWindow()
    sys.exit(app.exec())
