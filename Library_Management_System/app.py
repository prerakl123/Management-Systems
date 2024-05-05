from tkinter import Frame
from tkinter.constants import (
    NSEW,
    EW, N
)
from tkinter.font import BOLD

from customtkinter import (
    set_appearance_mode,
    set_widget_scaling,
    CTk,
    CTkLabel,
    CTkFont,
    CTkButton,
    CTkFrame,
    CTkOptionMenu,
    CTkScrollableFrame, CTkToplevel
)
from db import LibraryDB
from dotenv import load_dotenv

load_dotenv('.env')

IS_LOGGED_IN = False


class CTkSeparator(Frame):
    def __init__(self, master, **kwargs):
        Frame.__init__(self, master, **kwargs)
        self.configure(height=1)


class LoginFrame(CTkFrame):
    def __init__(self, parent, controller, **kwargs):
        CTkFrame.__init__(self, parent, **kwargs)
        self.controller = controller

        self.login_label = CTkLabel(self, text="Sign-In", font=CTkFont(size=22))

        self.username_label = CTkLabel(self, text="Username")

    def create_widgets(self):
        self.login_label.grid(row=0, column=0, columnspan=4, sticky=NSEW)


class RegisterFrame(CTkFrame):
    def __init__(self, parent, controller, **kwargs):
        CTkFrame.__init__(self, parent, **kwargs)
        self.controller = controller

    def create_widgets(self):
        pass


class BookFrame(CTkFrame):
    def __init__(self, parent, controller, book_metadata, **kwargs):
        CTkFrame.__init__(self, parent, controller, **kwargs)
        self.controller = controller
        self.database: LibraryDB = self.controller.database

        self.book_metadata = book_metadata
        self.book_name = book_metadata.get('title')
        self.genres = []
        for g in book_metadata.get('genres').split(';'):
            self.genres.append(self.database.get(
                table="genre",
                columns=["name"],
                where=[f"id={g}"]
            )[0])
        self.author = self.database.get(
            table="authors",
            columns=["name"],
            where=[f"id={book_metadata.get('author')}"]
        )
        self.publication_year = book_metadata.get('publication_year')
        self.isbn = book_metadata.get('isbn')
        self.availability = book_metadata.get('availability')
        self.borrowed_nums = self.database.get_from_query(f"SELECT COUNT(*) FROM `borrowed_books` WHERE bookid=")

    def create_widgets(self):
        pass


class AllBooksFrame(CTkFrame):
    def __init__(self, parent, controller, **kwargs):
        CTkFrame.__init__(self, parent, **kwargs)
        self.controller = controller

    def create_widgets(self):
        pass


class AddBooksWindow(CTkToplevel):
    def __init__(self, database: LibraryDB, *args, **kwargs):
        CTkToplevel.__init__(self, *args, **kwargs)
        self.database = database

    def create_widgets(self):
        pass


class EditBooksWindow(CTkToplevel):
    def __init__(self, database: LibraryDB, *args, **kwargs):
        CTkToplevel.__init__(self, *args, **kwargs)
        self.database = database

    def create_widgets(self):
        pass


class LibraryApp(CTk):
    def __init__(self, database: LibraryDB):
        CTk.__init__(self)

        self.database = database

        self.title("Library Management System")
        self.geometry("1200x630")

        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        # ----- SIDEBAR -----
        self.sidebar_frame = CTkFrame(self, width=200, corner_radius=5)

        self.logo_label = CTkLabel(self.sidebar_frame, text="LMS", font=CTkFont(size=20, weight=BOLD))

        self.sidebar_insert_btn = CTkButton(self.sidebar_frame, text="Insert New Book", command=lambda: print("Insert"))
        self.sidebar_update_btn = CTkButton(self.sidebar_frame, text="Update Book Details", command=lambda: print("Update"))
        self.sidebar_delete_btn = CTkButton(self.sidebar_frame, text="Remove a Book", command=lambda: print("Delete"))

        self.separator_1 = CTkSeparator(self.sidebar_frame, bg="#707070")

        self.sidebar_show_all_books_btn = CTkButton(self.sidebar_frame, text="Show All Books", command=self.show_all_books)

        self.appearance_mode_label = CTkLabel(self.sidebar_frame, text="Appearance Mode:", anchor="w")
        self.appearance_mode_optionmenu = CTkOptionMenu(self.sidebar_frame,
                                                        values=["Light", "Dark", "System"],
                                                        command=self.change_appearance_mode_event)

        self.scaling_label = CTkLabel(self.sidebar_frame, text="UI Scaling:", anchor="w")
        self.scaling_optionmenu = CTkOptionMenu(self.sidebar_frame,
                                                values=["100%", "70%", "80%", "90%", "110%", "120%", "150%"],
                                                command=self.change_scaling_event)

        # ----- MAIN FRAME ------
        self.update_idletasks()
        print(self.winfo_height(), self.winfo_width())
        self.container = CTkScrollableFrame(self, label_text="Login", width=self.winfo_width(), height=self.winfo_height())

        self.create_widgets()

        self.bind("<Configure>", self.on_any_event)

    def create_widgets(self):
        # Sidebar Frame widgets
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky=NSEW)
        self.sidebar_frame.grid_rowconfigure(4, weight=1)
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))

        self.sidebar_insert_btn.grid(row=1, column=0, padx=20, pady=10)
        self.sidebar_update_btn.grid(row=2, column=0, padx=20, pady=10)
        self.sidebar_delete_btn.grid(row=3, column=0, padx=20, pady=10)

        self.separator_1.grid(row=4, column=0, padx=20, pady=10, sticky=EW)

        self.sidebar_show_all_books_btn.grid(row=5, column=0, padx=20, pady=10)

        self.appearance_mode_label.grid(row=6, column=0, padx=20, pady=(10, 0))
        self.appearance_mode_optionmenu.grid(row=7, column=0, padx=20, pady=(10, 10))
        self.scaling_label.grid(row=8, column=0, padx=20, pady=(10, 0))
        self.scaling_optionmenu.grid(row=9, column=0, padx=20, pady=(10, 20))

        self.container.grid(row=0, column=5, padx=10, pady=5, sticky=NSEW)

    def change_appearance_mode_event(self, new_appearance_mode: str):
        set_appearance_mode(new_appearance_mode)

    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        set_widget_scaling(new_scaling_float)

    def on_any_event(self, _):
        self.update_idletasks()
        new_scale = int(self.scaling_optionmenu.get().rstrip("%")) / 100
        # print(new_scale, 220 * new_scale)
        if new_scale > 1:
            new_width = int((2.02 - new_scale) * (self.winfo_width() - (220 * new_scale)))
            new_height = self.winfo_height()
        elif new_scale < 1:
            new_width = int(self.winfo_width() + (self.winfo_width() * (1 - new_scale - 0.1)))
            new_height = int(self.winfo_height() + (self.winfo_height() * (1 - new_scale)))
        else:
            new_width = self.winfo_width() - 220
            new_height = self.winfo_height()

        print(new_width)
        self.container.configure(width=new_width, height=new_height)

    def show_frame(self, context):
        """
        Shows next required frame or page
        :param context: name of frame
        """
        frame = self.frames[context]
        frame.tkraise()
        self.update_idletasks()

    def remove_frame(self, context):
        """
        Removes unwanted frames from background
        :param context: name of frame
        """
        frame = self.frames[context]
        frame.forget()
        frame.grid_forget()
        self.update_idletasks()

    def get_famous_books(self):
        famous_books = self.database.get_from_query(
            "SELECT COUNT(*) " +
            "FROM `borrowed_books` " +
            "GROUP BY `bookid` DESC " +
            "LIMIT 5;"
        )
        if not famous_books:
            return "No borrowed books found!"

    def show_all_books(self):
        self.database.get(table="books", columns=["*"])


if __name__ == '__main__':
    db = LibraryDB()
    app = LibraryApp(database=db)
    set_appearance_mode('dark')
    app.bind("<Escape>", lambda event: app.attributes("-fullscreen", False))
    app.bind('<F11>', lambda event: app.attributes('-fullscree', True))
    # app.attributes('-fullscreen', True)
    app.mainloop()
