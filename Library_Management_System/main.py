from tkinter import *
from books import Books, BooksFrame
from user import User, UserFrame


class LMSystem(Tk):
    USERNAME: str = not None

    def __init__(self):
        Tk.__init__(self)

    def show_frame(self, frame: Frame):
        pass

    def remove_frame(self, frame: Frame):
        pass


def main():
    LMSystem().mainloop()


if __name__ == '__main__':
    main()

# add, edit, delete book (with reason), categories, search, settings (categories, authors, publishers), reports
