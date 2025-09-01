# ///////////////////////////////////////////////////////////////
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

        # USE CUSTOM TITLE BAR | USE AS "False" FOR MAC OR LINUX
        # ///////////////////////////////////////////////////////////////
        Settings.ENABLE_CUSTOM_TITLE_BAR = True

        # APP NAME
        # ///////////////////////////////////////////////////////////////
        title = "qsLAM_PCR_AIO"
        self.setWindowTitle(title)

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
        self.dragPos = event.globalPos()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("icon.ico"))
    window = MainWindow()
    sys.exit(app.exec_())
