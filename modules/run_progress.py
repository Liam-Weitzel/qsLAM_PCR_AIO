from PySide6.QtWidgets import QMessageBox, QDialog, QLabel, QVBoxLayout
from PySide6.QtGui import QMovie
from PySide6.QtCore import Qt, QSize, QPoint, QUrl
from PySide6.QtNetwork import QNetworkAccessManager, QNetworkRequest, QNetworkReply
from . settings import Settings

class RunProgress:
    def __init__(self, main_window):
        self.main_window = main_window
        self.widgets = main_window.ui
        self.spinner_dialog = None

        self.widgets.runButton.clicked.connect(self.start_run)
        self.widgets.cleanButton.clicked.connect(self.clean_run)
        self.widgets.pauseButton.clicked.connect(self.pause_run)
        self.widgets.resumeButton.clicked.connect(self.resume_run)

    def pause_run(self):
        QMessageBox.information(
            self.main_window,
            "Pausing Run",
            "The run will pause as soon as possible.\nPlease note this may take a few minutes."
        )

        self.show_spinner_dialog()

        # Make async HTTP GET request to test connectivity (simulate waiting for backend)
        request = QNetworkRequest(QUrl("https://www.google.com"))
        reply = self.main_window.network_manager.get(request)
        reply.finished.connect(lambda: self.handle_pause_reply(reply))

    def handle_pause_reply(self, reply: QNetworkReply):
        if reply.error() == QNetworkReply.NetworkError.NoError:
            # Successful "ping"
            Settings.METADATA.set("isPaused", True)
        else:
            # Error occurred (no internet or other issue)
            QMessageBox.warning(
                self.main_window,
                "Pause Error",
                f"Failed to reach the server. Error: {reply.errorString()}"
            )

        reply.deleteLater()
        self.hide_spinner_dialog()
        self.load_from_metadata()

    def clean_run(self):
        reply = QMessageBox.question(
            self.main_window,
            "Confirm Cleanup",
            "Are you sure you want to clean this run?\nThis will reset all progress made so far.",
            QMessageBox.Yes | QMessageBox.No
        )

        if reply == QMessageBox.Yes:
            Settings.METADATA.set("isRunning", False)
            self.load_from_metadata()

    def start_run(self):
        Settings.METADATA.set("isRunning", True)
        self.load_from_metadata()

    def resume_run(self):
        Settings.METADATA.set("isPaused", False)
        self.load_from_metadata()

    def load_from_metadata(self):
        is_running = Settings.METADATA.get("isRunning", False)
        is_paused = Settings.METADATA.get("isPaused", False)

        if is_running:
            self.widgets.progressBar.show()
            self.widgets.runButton.hide()
            self.widgets.cleanButton.show()

            if is_paused:
                self.widgets.progressBar.setEnabled(False)
                self.widgets.progressBar.setStyleSheet("""
                    QProgressBar {
                        background-color: #ddd;
                        border: 1px solid #aaa;
                        background-image: url(':/icons/images/icons/cil-media-pause.png');
                        background-repeat: no-repeat;
                        background-position: center;
                        color: transparent;
                    }
                    QProgressBar::chunk {
                        background-color: #aaa;
                    }
                """)
                self.widgets.pauseButton.hide()
                self.widgets.resumeButton.show()
            else:
                self.widgets.progressBar.setEnabled(True)
                self.widgets.progressBar.setStyleSheet("""
                    QProgressBar {
                        border: 1px solid #bbb;
                        background: #eee;
                        text-align: center;
                    }
                    QProgressBar::chunk {
                        background-color: #86D2ED;
                    }
                """)
                self.widgets.pauseButton.show()
                self.widgets.resumeButton.hide()
        else:
            self.widgets.progressBar.hide()
            self.widgets.runButton.show()
            self.widgets.pauseButton.hide()
            self.widgets.resumeButton.hide()
            self.widgets.cleanButton.hide()

    def show_spinner_dialog(self):
        self.spinner_dialog = QDialog(self.main_window)
        self.spinner_dialog.setModal(True)
        self.spinner_dialog.setWindowFlags(Qt.WindowType.Dialog | Qt.WindowType.FramelessWindowHint)
        self.spinner_dialog.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)

        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.setContentsMargins(20, 20, 20, 20)

        spinner = QLabel()
        movie = QMovie(":/images/images/images/spinner.gif")
        movie.setScaledSize(QSize(80, 80))
        spinner.setMovie(movie)
        movie.start()

        layout.addWidget(spinner)
        self.spinner_dialog.setLayout(layout)
        self.spinner_dialog.adjustSize()

        parent_center = self.main_window.geometry().center()
        dialog_size = self.spinner_dialog.size()
        self.spinner_dialog.move(parent_center - QPoint(dialog_size.width() // 2, dialog_size.height() // 2))

        self.spinner_dialog.show()

    def hide_spinner_dialog(self):
        if self.spinner_dialog:
            self.spinner_dialog.accept()
            self.spinner_dialog = None
