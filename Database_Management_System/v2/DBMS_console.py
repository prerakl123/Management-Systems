import sys
import os
import pandas
import sqlite3
import ctypes
import rich
from colors import (
    CEND, CBOLD, CITALIC, CURL, CBLINK, CBLINK2, CSELECTED, CBLACK, CRED, CGREEN, CYELLOW, CBLUE, CVIOLET,
    CBEIGE, CWHITE, CBLACKBG, CREDBG, CGREENBG, CYELLOWBG, CBLUEBG, CVIOLETBG, CBEIGEBG, CWHITEBG, CGREY,
    CRED2, CGREEN2, CYELLOW2, CBLUE2, CVIOLET2, CBEIGE2, CWHITE2, CGREYBG, CREDBG2, CGREENBG2, CYELLOWBG2,
    CBLUEBG2, CVIOLETBG2, CBEIGEBG2, CWHITEBG2
)

ctypes.windll.kernel32.SetConsoleTitleW("Database Management - Console")

ADD = 'add'
CREATE = 'create'
DB = 'db'
DATABASE = 'database'
DELETE = 'delete'
DISPLAY = 'display'
EXIT = 'exit'
SET = 'set'
SEARCH = 'search'
TABLE = 'table'
UPDATE = 'update'


class DataBaseManagementSystem:
    def __init__(self):
        self.db = None

    def create_db(self, name: str) -> tuple[bool, str]:
        pass

    def create_table(self, name: str) -> tuple[bool, str]:
        pass

    def display_command(self):
        while True:
            command = list(map(str, input('DBMS> ').split()))
            if command[0].lstrip().rstrip() == EXIT:
                break
            elif command[0] == CREATE:
                if command[1] == DB or command[1] == DATABASE:
                    pass
                elif command[1] == TABLE:


def main():
    # os.system('cls')
    rich.print('[blink]Color[/] in the [bold magenta]Terminal[/]!')
    print('\033[91mAloopakoda\033[0m')
    input()


if __name__ == '__main__':
    main()
