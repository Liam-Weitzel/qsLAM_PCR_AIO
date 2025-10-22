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
        self.settings = Settings()
        self.network_manager = QNetworkAccessManager()

        # APP NAME
        # ///////////////////////////////////////////////////////////////
        self.setWindowTitle(Settings.TITLE)

        # TOGGLE MENU
        # ///////////////////////////////////////////////////////////////
        widgets.toggleButton.clicked.connect(lambda: UIFunctions.toggleMenu(self, True))

        # SET UI DEFINITIONS
        # ///////////////////////////////////////////////////////////////
        UIFunctions.uiDefinitions(self)

        # INIT ALL TABS
        # ///////////////////////////////////////////////////////////////
        self.run_manager = RunManager(self)
        self.run_progress = RunProgress(self)
        self.run_configuration = RunConfiguration(self)
        self.results_overview = ResultsOverview(self)

        # BUTTONS CLICK - CONNECT EACH TO ITS OWN HANDLER
        # ///////////////////////////////////////////////////////////////

        # LEFT MENUS
        widgets.runManagerButton.clicked.connect(lambda: self.on_menu_button_clicked(widgets.runManagerTab, widgets.runManagerButton, "runManagerButton"))
        widgets.runConfigurationButton.clicked.connect(lambda: self.on_menu_button_clicked(widgets.runConfigurationTab, widgets.runConfigurationButton, "runConfigurationButton"))
        widgets.runProgressButton.clicked.connect(lambda: self.on_menu_button_clicked(widgets.runProgressTab, widgets.runProgressButton, "runProgressButton"))
        widgets.resultsOverviewButton.clicked.connect(lambda: self.on_menu_button_clicked(widgets.resultsOverviewTab, widgets.resultsOverviewButton, "resultsOverviewButton"))

        # EXTRA LEFT BOX
        widgets.toggleLeftBox.clicked.connect(lambda: UIFunctions.toggleLeftBox(self, True))
        widgets.extraCloseColumnButton.clicked.connect(lambda: UIFunctions.toggleLeftBox(self, True))

        # EXTRA RIGHT BOX
        widgets.settingsTopButton.clicked.connect(lambda: UIFunctions.toggleRightBox(self, True))
        widgets.moreButton.clicked.connect(lambda: QDesktopServices.openUrl(QUrl("https://www.erasmusmc.nl/en/pages/about-erasmusmc")))

        # SHOW APP
        # ///////////////////////////////////////////////////////////////
        self.show()
        self.show_first_time_dialog()

        # INIT STATE
        self.disable_button(widgets.runProgressButton)
        self.disable_button(widgets.runConfigurationButton)
        self.disable_button(widgets.resultsOverviewButton)

    # HANDLER FOR LEFT MENU BUTTONS
    # ///////////////////////////////////////////////////////////////
    def on_menu_button_clicked(self, tab_widget, button_widget, button_name, show_selected_run=True):
        widgets.stackedWidget.setCurrentWidget(tab_widget)
        UIFunctions.resetStyle(self, button_name)
        button_widget.setStyleSheet(UIFunctions.selectMenu(button_widget.styleSheet()))
        
        if show_selected_run:
            widgets.currentlySelectedText.setText("Currently Selected Run: ")
            widgets.currentlySelected.setText(Settings.SELECTED_RUN or "None")
        else:
            widgets.currentlySelectedText.setText("")
            widgets.currentlySelected.setText("")

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
    
    # DISABLE BUTTONS
    # ///////////////////////////////////////////////////////////////
    def disable_button(self, button):
        # Prevent re-disabling
        if button.property("is_custom_disabled"):
            return

        # Set cursor
        button.setCursor(QCursor(Qt.CursorShape.WhatsThisCursor))

        # Modify style only if not already applied
        current_style = button.styleSheet()

        if "background-color: lightgrey;" not in current_style:
            current_style += " background-color: lightgrey;"

        if "-cross.png" not in current_style:
            current_style = current_style.replace(".png", "-cross.png")

        button.setStyleSheet(current_style)

        # Set tooltip
        button.setToolTip(QCoreApplication.translate(
            "MainWindow", u"        Select a run and configure it in order to progress", None))

        # Replace clicked handler
        try:
            button.clicked.disconnect()
        except TypeError:
            pass
        button.clicked.connect(self.show_disabled_dialog)

        # Set custom property
        button.setProperty("is_custom_disabled", True)

    def enable_button(self, button, func):
        # Prevent re-enabling if not disabled
        if not button.property("is_custom_disabled"):
            return

        # Set cursor
        button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        # Clean up style
        current_style = button.styleSheet()
        current_style = current_style.replace(" background-color: lightgrey;", "")
        current_style = current_style.replace("-cross.png", ".png")
        button.setStyleSheet(current_style)

        # Remove tooltip
        button.setToolTip("")

        # Restore original clicked function
        try:
            button.clicked.disconnect()
        except TypeError:
            pass
        button.clicked.connect(func)

        # Remove the custom disabled state
        button.setProperty("is_custom_disabled", False)

    def show_disabled_dialog(self):
        msg_box = QMessageBox(self)
        msg_box.setWindowTitle("Tab is not available")
        msg_box.setText("Please select a run and save its run configurations in order to progress")
        msg_box.setIcon(QMessageBox.Information)
        msg_box.setStandardButtons(QMessageBox.Ok)
        msg_box.exec_()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("icon.ico"))
    window = MainWindow()
    sys.exit(app.exec())
