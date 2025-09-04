import json
import os
from . settings import Settings
from datetime import datetime

class Metadata:
    DEFAULTS = {
        "creation_timestamp": datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    }

    def __init__(self, run):
        self.run_path = os.path.join(Settings.RUNS_DIR, run)
        if not os.path.isdir(self.run_path):
            raise FileNotFoundError(f"[Metadata] Run directory does not exist: {self.run_path}")

        self.metadata_path = os.path.join(self.run_path, Settings.METADATA_FILE)

        self._data = {}
        
        if os.path.exists(self.metadata_path):
            self._load()
        else:
            self._data = dict(self.DEFAULTS)
            self.save()

    def _load(self):
        if os.path.exists(self.metadata_path):
            try:
                with open(self.metadata_path, "r") as f:
                    self._data = json.load(f)
            except Exception as e:
                raise RuntimeError(f"[Metadata] Failed to load metadata from {self.metadata_path}: {e}")
        else:
            raise FileNotFoundError(f"[Metadata] Metadata file not found: {self.metadata_path}")

    def save(self):
        try:
            with open(self.metadata_path, "w") as f:
                json.dump(self._data, f, indent=2)
        except Exception as e:
            raise RuntimeError(f"[Metadata] Failed to save metadata to {self.metadata_path}: {e}")

    def get(self, key, default=None):
        return self._data.get(key, default)

    def set(self, key, value):
        self._data[key] = value
        self.save()

    def delete(self, key):
        if key in self._data:
            del self._data[key]
            self.save()

    def to_dict(self):
        return dict(self._data)

    def update(self, data: dict):
        self._data.update(data)
        self.save()
