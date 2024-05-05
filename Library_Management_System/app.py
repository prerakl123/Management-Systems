from tkinter import Frame
from tkinter.constants import (
    NSEW,
    EW,
    N,
    BOTH,
    X,
    NW, DISABLED
)
from tkinter.font import (
    BOLD,
    NORMAL
)

from customtkinter import (
    set_appearance_mode,
    set_widget_scaling,
    CTk,
    CTkLabel,
    CTkFont,
    CTkButton,
    CTkFrame,
    CTkOptionMenu,
    CTkScrollableFrame,
    CTkToplevel,
    CTkEntry
)
from db import LibraryDB
from dotenv import load_dotenv

load_dotenv('.env')

IS_LOGGED_IN = False
HEADING_FONT = {"family": "Cascadia Code", "size": 24, "weight": NORMAL}
LABEL_FONT = {"family": "Cascadia Code", "size": 16, "weight": BOLD}
ENTRY_FONT = {"family": "Cascadia Code SemiLight", "size": 16, "weight": NORMAL}
BUTTON_FONT = {"family": "Cascadia Code", "size": 16, "weight": NORMAL}


class CTkSeparator(Frame):
    def __init__(self, master, **kwargs):
        Frame.__init__(self, master, **kwargs)
        self.configure(height=1, bg="#707070")


class LoginFrame(CTkFrame):
    def __init__(self, parent, controller, **kwargs):
        CTkFrame.__init__(self, parent, **kwargs)
        self.controller = controller
        self.container_label_text = "Authentication"

        self.login_label = CTkLabel(self, text="Sign-In", font=CTkFont(**HEADING_FONT))

        self.entry_frame = CTkFrame(self, width=350, height=250)
        self.username_label = CTkLabel(self.entry_frame, text="Username", font=CTkFont(**LABEL_FONT))
        self.username_entry = CTkEntry(
            self.entry_frame,
            placeholder_text="Enter username",
            font=CTkFont(**ENTRY_FONT),
            width=250, height=35
        )

        self.password_label = CTkLabel(self.entry_frame, text="Password", font=CTkFont(**LABEL_FONT))
        self.password_entry = CTkEntry(
            self.entry_frame,
            width=250, height=35, show="•",
            placeholder_text="Enter password",
            font=CTkFont(**ENTRY_FONT))

        self.proceed_btn = CTkButton(self.entry_frame, text="Sign-In", font=CTkFont(**BUTTON_FONT), width=250)
        self.separator = CTkSeparator(self.entry_frame, width=150)

        self.register_label = CTkLabel(self.entry_frame, text="New User?", font=CTkFont(**LABEL_FONT))
        self.register_btn = CTkButton(self.entry_frame, text="Register", width=250, command=self.register_redirect, font=CTkFont(**BUTTON_FONT))

    def create_widgets(self):
        self.login_label.pack(anchor=N, fill=X, pady=(30, 20))

        self.entry_frame.pack(anchor=N, ipady=30, ipadx=30)

        self.username_label.pack(padx=(60, 0), pady=(40, 0), anchor=NW)
        self.username_entry.pack(padx=(60, 0), anchor=NW)

        self.password_label.pack(padx=(60, 0), pady=(20, 0), anchor=NW)
        self.password_entry.pack(padx=(60, 0), anchor=NW)

        self.proceed_btn.pack(padx=(60, 0), pady=(20, 0), anchor=NW, ipady=5)
        self.separator.pack(padx=(0, 0), pady=(40, 0), anchor=N)

        self.register_label.pack(padx=(0, 0), pady=(20, 0), anchor=N)
        self.register_btn.pack(padx=(60, 0), anchor=NW, ipady=5)

    def register_redirect(self):
        self.controller.remove_frame(self.controller.current_frame)
        self.controller.show_frame(RegisterFrame)
        self.controller.current_frame = RegisterFrame

    def check_login(self):
        pass


class RegisterFrame(CTkFrame):
    def __init__(self, parent, controller, **kwargs):
        CTkFrame.__init__(self, parent, **kwargs)
        self.controller = controller
        self.container_label_text = "Authentication"
        self.configure(bg_color="blue")

        self.register_label = CTkLabel(self, text="Register", font=CTkFont(**HEADING_FONT))

        self.entry_frame = CTkFrame(self, width=350, height=250)
        self.librarian_label = CTkLabel(self.entry_frame, text="Librarian Name", font=CTkFont(**LABEL_FONT))
        self.librarian_entry = CTkEntry(
            self.entry_frame,
            placeholder_text="Enter full name",
            font=CTkFont(**ENTRY_FONT),
            width=350, height=35
        )

        self.username_label = CTkLabel(self.entry_frame, text="Librarian Username", font=CTkFont(**LABEL_FONT))
        self.username_entry = CTkEntry(
            self.entry_frame,
            placeholder_text="Enter unique username",
            font=CTkFont(**ENTRY_FONT),
            width=350, height=35
        )

        self.password_label = CTkLabel(self.entry_frame, text="Password", font=CTkFont(**LABEL_FONT))
        self.password_entry = CTkEntry(
            self.entry_frame,
            placeholder_text="Enter password",
            font=CTkFont(**ENTRY_FONT),
            width=350, height=35, show="•"
        )

        self.password2_label = CTkLabel(self.entry_frame, text="Confirm Password", font=CTkFont(**LABEL_FONT))
        self.password2_entry = CTkEntry(
            self.entry_frame,
            placeholder_text="Re-enter password to confirm",
            font=CTkFont(**ENTRY_FONT),
            width=350, height=35, show="•"
        )

        self.proceed_btn = CTkButton(self.entry_frame, text="Register", width=350, command=self.check_registration, font=CTkFont(**BUTTON_FONT))
        self.separator = CTkSeparator(self.entry_frame, width=150)

        self.login_label = CTkLabel(self.entry_frame, text="Already registered?", font=CTkFont(**LABEL_FONT))
        self.login_btn = CTkButton(self.entry_frame, text="Login", width=350, command=self.login_redirect, font=CTkFont(**BUTTON_FONT))

    def create_widgets(self):
        self.register_label.pack(anchor=N, fill=X, pady=(30, 20))

        self.entry_frame.pack(ipadx=30, ipady=30, anchor=N)
        self.librarian_label.pack(padx=(60, 0), pady=(45, 5), anchor=NW)
        self.librarian_entry.pack(padx=(60, 0), anchor=NW)

        self.username_label.pack(padx=(60, 0), pady=(25, 5), anchor=NW)
        self.username_entry.pack(padx=(60, 0), anchor=NW)

        self.password_label.pack(padx=(60, 0), pady=(25, 5), anchor=NW)
        self.password_entry.pack(padx=(60, 0), anchor=NW)

        self.password2_label.pack(padx=(60, 0), pady=(25, 5), anchor=NW)
        self.password2_entry.pack(padx=(60, 0), anchor=NW)

        self.proceed_btn.pack(padx=(60, 0), pady=(25, 5), anchor=NW, ipady=5)
        self.separator.pack(padx=(0, 0), pady=(45, 5), anchor=N)

        self.login_label.pack(padx=(0, 0), pady=(25, 10), anchor=N)
        self.login_btn.pack(padx=(60, 0), anchor=NW, ipady=5)

    def login_redirect(self):
        self.controller.remove_frame(self.controller.current_frame)
        self.controller.show_frame(LoginFrame)
        self.controller.current_frame = LoginFrame

    def check_registration(self):
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
        self.borrowed_nums = self.database.get_from_query(
            f"SELECT COUNT(*) FROM `borrowed_books` WHERE bookid={book_metadata.get('id')}"
        )[0]

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

        self.sidebar_insert_btn = CTkButton(self.sidebar_frame, text="Insert New Book", width=200, font=CTkFont(**BUTTON_FONT), state=DISABLED, command=lambda: print("Insert"))
        self.sidebar_update_btn = CTkButton(self.sidebar_frame, text="Update Book Details", width=200, font=CTkFont(**BUTTON_FONT), state=DISABLED, command=lambda: print("Update"))
        self.sidebar_delete_btn = CTkButton(self.sidebar_frame, text="Remove a Book", width=200, font=CTkFont(**BUTTON_FONT), state=DISABLED, command=lambda: print("Delete"))

        self.separator_1 = CTkSeparator(self.sidebar_frame)

        self.sidebar_show_all_books_btn = CTkButton(self.sidebar_frame, text="Show All Books", width=200, font=CTkFont(**BUTTON_FONT), state=DISABLED, command=self.show_all_books)

        self.appearance_mode_label = CTkLabel(self.sidebar_frame, text="Appearance Mode:", anchor="w", font=CTkFont(family="Cascadia Code", weight=BOLD))
        self.appearance_mode_optionmenu = CTkOptionMenu(self.sidebar_frame, width=200,
                                                        values=["Dark", "Light", "System"],
                                                        command=self.change_appearance_mode_event)

        self.scaling_label = CTkLabel(self.sidebar_frame, text="UI Scaling:", anchor="w", font=CTkFont(family="Cascadia Code", weight=BOLD))
        self.scaling_optionmenu = CTkOptionMenu(self.sidebar_frame, width=200,
                                                values=["100%", "70%", "80%", "90%", "110%", "120%", "150%"],
                                                command=self.change_scaling_event)

        self.separator_2 = CTkSeparator(self.sidebar_frame)

        self.logout_btn = CTkButton(self.sidebar_frame, text="Logout", width=200, font=CTkFont(**BUTTON_FONT), fg_color="#bd2d2d", hover_color="#821010", command=self.logout)

        self.update_idletasks()

        # ----- MAIN FRAME ------
        self.container = CTkScrollableFrame(self, label_text="Login", width=self.winfo_width(), height=self.winfo_height())
        self.current_frame = LoginFrame
        self.frames = {}
        self.frame_classes = (RegisterFrame, LoginFrame, AllBooksFrame)
        for f in self.frame_classes:
            frame = f(self.container, self)
            self.frames[f] = frame
            frame.create_widgets()
            # frame.pack(expand=True, fill=BOTH, anchor=N)

        self.create_widgets()
        self.show_frame(LoginFrame)

        self.bind("<Configure>", self.on_any_event)

    def create_widgets(self):
        # Sidebar Frame widgets
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky=NSEW)
        self.sidebar_frame.grid_rowconfigure(4, weight=1)
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))

        self.sidebar_insert_btn.grid(row=1, column=0, padx=20, pady=10, ipady=5)
        self.sidebar_update_btn.grid(row=2, column=0, padx=20, pady=10, ipady=5)
        self.sidebar_delete_btn.grid(row=3, column=0, padx=20, pady=10, ipady=5)

        self.separator_1.grid(row=4, column=0, padx=20, pady=10, sticky=EW)

        self.sidebar_show_all_books_btn.grid(row=5, column=0, padx=20, pady=10, ipady=5)

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

        if new_scale > 1:
            new_width = int((2.02 - new_scale) * (self.winfo_width() - (270 * new_scale)))
            new_height = self.winfo_height()
        elif new_scale < 1:
            new_width = int(self.winfo_width() + (self.winfo_width() * (1 - new_scale - 0.12)))
            new_height = int(self.winfo_height() + (self.winfo_height() * (1 - new_scale)))
        else:
            new_width = self.winfo_width() - 270
            new_height = self.winfo_height()

        self.container.configure(width=new_width, height=new_height)

    def show_frame(self, context):
        """
        Shows next required frame or page
        :param context: name of frame
        """
        frame = self.frames[context]
        frame.tkraise()
        frame.pack(expand=True, fill=BOTH, anchor=N)
        self.container.configure(label_text=frame.container_label_text)
        self.update_idletasks()

    def remove_frame(self, context):
        """
        Removes unwanted frames from background
        :param context: name of frame
        """
        frame = self.frames[context]
        frame.forget()
        frame.pack_forget()
        self.update_idletasks()

    def enable_sidebar_buttons(self):
        self.sidebar_insert_btn.configure(state=NORMAL)
        self.sidebar_update_btn.configure(state=NORMAL)
        self.sidebar_delete_btn.configure(state=NORMAL)
        self.sidebar_show_all_books_btn.configure(state=NORMAL)

    def add_logout_btn(self):
        self.separator_2.grid(row=10, column=0, padx=20, pady=10, sticky=EW)
        self.logout_btn.grid(row=11, column=0, padx=20, pady=(10, 20))

    def logout(self):
        global IS_LOGGED_IN
        IS_LOGGED_IN = False

        self.remove_frame(self.current_frame)
        self.show_frame(LoginFrame)
        self.current_frame = LoginFrame

        self.separator_2.grid_forget()
        self.logout_btn.grid_forget()

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
