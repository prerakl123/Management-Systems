from tkinter import *
from tkinter import messagebox as tk_mb
from tkinter import scrolledtext as tk_st
from tkinter import filedialog as tk_fd
import windnd
import json


class Window:
    def __init__(self, root):
        self.root = root


def main():
    root = Tk()
    app = Window(root)


if __name__ == '__main__':
    main()
