import sqlite3
import json
from typing import TextIO


class DBFileNotFoundError(Exception):
    pass


class ConfigJSON:
    def __init__(self):
        self.db_dict = dict()

    def already_json(self, file: str):
        self.db_dict = json.loads(open(file, 'r').read())

    def open_file(self):
        try:
            self.db_dict = json.loads(open('dbconfig.json', 'r').read())
        except FileNotFoundError:
            raise DBFileNotFoundError

    def read_json(self):
        pass

    def write_to_json(self):
        pass


class ConfigDB:
    def __init__(self):
        pass

    def add_records(self, *command):
        pass

    def add_custom_records(self, *command):
        pass

    def get_records(self, *command):
        pass
