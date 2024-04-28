from customtkinter import (
    set_appearance_mode,
    CTk,
    CTkFrame
)
from dotenv import load_dotenv

load_dotenv('.env')


class LibraryApp(CTk):
    window_frame: CTkFrame

    def __init__(self):
        CTk.__init__(self)

    def create_widgets(self):
        self.window_frame = CTkFrame(self, corner_radius=5, border_width=0)


if __name__ == '__main__':
    app = LibraryApp()
    set_appearance_mode('dark')
    app.mainloop()
