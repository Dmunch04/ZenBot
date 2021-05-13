import json
from typing import Dict, Any


class Config:
    def __init__(self, conf_path: str):
        self.conf_path = conf_path
        with open(conf_path, "r") as config_file:
            self.data = json.load(config_file)

    def get(self, key: str, alt: Any = None):
        return self.data.get(key, alt)

    @property
    def config(self) -> Dict[str, Any]:
        return self.data

    @property
    def bot_description(self) -> str:
        return self.data.get("description", "")

    @property
    def status(self) -> str:
        return self.data.get("status", "")

    @property
    def invite(self) -> str:
        return self.data.get("invite", "")

    @property
    def db_config(self) -> Dict[str, str]:
        return self.data.get("db", {})


config = Config("./config.json")
