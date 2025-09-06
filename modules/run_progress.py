from . settings import Settings

class RunProgress:
    def __init__(self, main_window):
        self.settings = Settings()
        self.main_window = main_window
        self.widgets = main_window.ui
