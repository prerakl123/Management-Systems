from tkinter import Frame


class User:
    def __init__(self, win):
        pass


class UserFrame(Frame):
    def __init__(self, master, **kw):
        Frame.__init__(self, **kw)

    def show_frame(self, frame: Frame):
        pass

    def remove_frame(self, frame: Frame):
        pass

# User frame can contain login, sign-up, book preferences,
