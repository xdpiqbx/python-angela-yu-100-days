import os
import json
from pathlib import Path


class FileManager:
    def __init__(self, filename):
        self.SAVE_TO = "./already_requested/"
        self.filename = filename
        self.data_must_be_requested = True

    def is_current_file_exists(self) -> None:
        for filename in os.listdir(self.SAVE_TO):
            if filename == self.filename:
                self.data_must_be_requested = False
                break

    def is_necessary_to_request(self) -> bool:
        return self.data_must_be_requested

    def save_to_json(self, data):
        with open(Path(self.SAVE_TO, self.filename), 'w') as json_file:
            json.dump(data, json_file, indent=4)

    def get_from_json(self):
        with open(Path(self.SAVE_TO, self.filename)) as json_file:
            return json.loads(json_file.read())
