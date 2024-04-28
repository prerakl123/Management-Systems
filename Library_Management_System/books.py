from tkinter import Frame


class Books:
    def __init__(self, win):
        pass


class BooksFrame(Frame):
    def __init__(self, master, **kw):
        Frame.__init__(self, master, **kw)

    def show_frame(self, frame: Frame):
        pass

    def remove_frame(self, frame: Frame):
        pass


# Book frames can contain picture of book, name, description, author, category, creator tags, price, publisher,
# user tags, year of publishing,
