import json
import os

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
    METADATA = None
    REF_RENOMES_SHARE_TOKEN = "abXeB3WtcWdm63f"

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

        # Default dynamic settings
        self._data.setdefault("ENABLE_CUSTOM_TITLE_BAR", False)
        self._data.setdefault("FIRST_START", True)

        self.save()

    def save(self):
        try:
            with open(self.SETTINGS_PATH, "w") as f:
                json.dump(self._data, f, indent=2)
        except Exception as e:
            print(f"[Settings] Failed to save settings: {e}")

    # Instance-based
    def get(self, key, default=None):
        return self._data.get(key, default)

    def set(self, key, value):
        self._data[key] = value
        self.save()

    # Singleton helper
    @classmethod
    def _ensure_instance(cls):
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance

    # Class-level accessors (no self)
    @classmethod
    def get_noself(cls, key, default=None):
        inst = cls._ensure_instance()
        return inst._data.get(key, default)

    @classmethod
    def set_noself(cls, key, value):
        inst = cls._ensure_instance()
        inst._data[key] = value
        inst.save()
