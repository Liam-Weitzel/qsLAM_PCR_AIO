import json
import os

# NOTE: Usage Example
# settings = Settings()
# # Read dynamic setting ENABLE_CUSTOM_TITLE_BAR
# use_custom_title = settings.get("ENABLE_CUSTOM_TITLE_BAR")
# print("Custom title bar enabled?", use_custom_title)
# # Change it and save
# settings.set("ENABLE_CUSTOM_TITLE_BAR", True)

class Settings:
    MENU_WIDTH = 240
    LEFT_BOX_WIDTH = 240
    RIGHT_BOX_WIDTH = 240
    TIME_ANIMATION = 200

    TITLE = "qsLAM_PCR_AIO"
    BTN_LEFT_BOX_COLOR = "background-color: #86D2ED"
    BTN_RIGHT_BOX_COLOR = "background-color: #86D2ED;"

    MENU_SELECTED_STYLESHEET = """
    border-left: 22px solid qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #0C2174, stop:0.5 rgba(0, 0, 0, 0));
    background-color: #86D2ED;
    """
    SIZE_GRIP_STYLESHEET = "width: 20px; height: 20px; margin 0px; padding: 0px;"

    SETTINGS_PATH = "settings.json"

    RUNS_DIR = "./runs/"
    SELECTED_RUN = None
    METADATA_FILE = "metadata.json"

    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._data = {}
            cls._instance._load()
        return cls._instance

    def _load(self):
        if os.path.exists(self.SETTINGS_PATH):
            try:
                with open(self.SETTINGS_PATH, "r") as f:
                    self._data = json.load(f)
            except Exception as e:
                print(f"[Settings] Failed to load settings: {e}")
                self._data = {}
        else:
            self._data = {}

        # Set default values for dynamic settings if missing
        if "ENABLE_CUSTOM_TITLE_BAR" not in self._data:
            self._data["ENABLE_CUSTOM_TITLE_BAR"] = False
        if "FIRST_START" not in self._data:
            self._data["FIRST_START"] = True

        self.save()

    def save(self):
        try:
            with open(self.SETTINGS_PATH, "w") as f:
                json.dump(self._data, f, indent=2)
        except Exception as e:
            print(f"[Settings] Failed to save settings: {e}")

    def get(self, key, default=None):
        return self._data.get(key, default)

    def set(self, key, value):
        self._data[key] = value
        self.save()
