from tkinter import Frame
from tkinter.constants import (
    NSEW,
    EW,
    N,
    BOTH,
    X,
    NW,
    DISABLED,
    W
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
from werkzeug.security import generate_password_hash, check_password_hash

load_dotenv('.env')

IS_LOGGED_IN = False
HEADING_FONT = {"family": "Cascadia Code", "size": 24, "weight": NORMAL}
LABEL_FONT = {"family": "Cascadia Code", "size": 16, "weight": BOLD}
ENTRY_FONT = {"family": "Cascadia Code SemiLight", "size": 16, "weight": NORMAL}
BUTTON_FONT = {"family": "Cascadia Code", "size": 16, "weight": NORMAL}
PRINTABLE_CHARS = (
    [chr(i) for i in range(97, 123)] +
    [chr(i) for i in range(65, 91)] +
    list("\\|]}[{'\";:/?.>,<=+-_)(*&^%$#@!") +
    list("1234567890")
)


class CTkSeparator(Frame):
    def __init__(self, master, **kwargs):
        Frame.__init__(self, master, **kwargs)
        self.configure(height=1, bg="#707070")


class LoginFrame(CTkFrame):
    def __init__(self, parent, controller, **kwargs):
        CTkFrame.__init__(self, parent, **kwargs)
        self.controller = controller
        self.database: LibraryDB = self.controller.database
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
        self.username_entry.bind("<KeyPress>", self.check_username_password)
        self.username_entry.bind("<KeyRelease>", self.check_username_password)

        self.password_label = CTkLabel(self.entry_frame, text="Password", font=CTkFont(**LABEL_FONT))
        self.password_entry = CTkEntry(
            self.entry_frame,
            width=250, height=35, show="•",
            placeholder_text="Enter password",
            font=CTkFont(**ENTRY_FONT))

        self.proceed_btn = CTkButton(self.entry_frame, text="Sign-In", font=CTkFont(**BUTTON_FONT), width=250, command=self.check_login)
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
        global IS_LOGGED_IN

        if self.check_username_password(None):
            IS_LOGGED_IN = True
            self.controller.remove_frame(self.controller.current_frame)
            self.controller.show_frame(AllBooksFrame)
            self.controller.current_frame = AllBooksFrame
            self.controller.add_logout_btn()
            self.controller.enable_sidebar_buttons()
        else:
            self.password_entry.configure(border_width=1, border_color="#ed4242")

    def check_username_password(self, _) -> bool:
        fetched_username = self.database.get(
            table="librarian",
            columns=["username", "passhash"],
            where=[f'username="{self.username_entry.get()}"'],
            limit=1
        )
        if len(fetched_username) < 1:
            self.username_entry.configure(border_width=1, border_color="#ed4242")
            return False
        else:
            self.username_entry.configure(border_width=1, border_color="#3ea82c")

        return check_password_hash(fetched_username[0][1], self.password_entry.get())


class RegisterFrame(CTkFrame):
    def __init__(self, parent, controller, **kwargs):
        CTkFrame.__init__(self, parent, **kwargs)
        self.controller = controller
        self.database: LibraryDB = self.controller.database
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
        self.username_entry.bind("<KeyPress>", self.check_unique_username)
        self.username_entry.bind("<KeyRelease>", self.check_unique_username)

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
        self.password2_entry.bind("<KeyPress>", self.check_password_equivalence)
        self.password2_entry.bind("<KeyRelease>", self.check_password_equivalence)
        self.password2_entry.bind("<BackSpace>", self.check_password_equivalence)
        self.password2_entry.bind("<space>", self.check_password_equivalence)

        self.proceed_btn = CTkButton(self.entry_frame, text="Register", width=350, command=self.check_registration, font=CTkFont(**BUTTON_FONT))
        self.separator = CTkSeparator(self.entry_frame, width=200)

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
        if self.check_password_equivalence(None) and self.check_unique_username(None):
            self.database.insert(
                (
                    self.librarian_entry.get(),
                    self.username_entry.get(),
                    generate_password_hash(self.password_entry.get())
                ),
                table="librarian",
                columns=["name", "username", "passhash"]
            )
            self.controller.remove_frame(self.controller.current_frame)
            self.controller.show_frame(LoginFrame)
            self.controller.current_frame = LoginFrame

    def check_password_equivalence(self, _) -> bool:
        if self.password_entry.get() != self.password2_entry.get():
            self.password_entry.configure(border_color="#ed4242", border_width=1)
            self.password2_entry.configure(border_color="#ed4242", border_width=1)
            return False
        else:
            self.password_entry.configure(border_color="#3ea82c", border_width=1)
            self.password2_entry.configure(border_color="#3ea82c", border_width=1)
            return True

    def check_unique_username(self, _) -> bool:
        entered_username = self.username_entry.get()
        if len(entered_username) < 5 or entered_username[0].isnumeric():
            self.username_entry.configure(border_width=1, border_color="#ed4242")
            return False

        usernames = self.database.get(
            table="librarian",
            columns=["username"],
            where=["username", "LIKE", f'"{entered_username}%"']
        )
        usernames = list(map(lambda x: x[0], usernames))
        if entered_username in usernames:
            self.username_entry.configure(border_width=1, border_color="#ed4242")
            return False
        else:
            self.username_entry.configure(border_width=1, border_color="#3ea82c")
            return True


class DashboardFrame(CTkFrame):
    def __init__(self, parent, controller, **kwargs):
        CTkFrame.__init__(self, parent, **kwargs)
        self.controller = controller
        self.database: LibraryDB = self.controller.database
        self.container_label_text = "Dashboard"

        self.frame_list = []
        self.create_all_frames()

    def get_data(self) -> list[dict]:
        return [
            {
                "title": "Librarians",
                "subtitle": "No. of available librarians",
                "number": self.database.get_from_query("SELECT COUNT(*) FROM librarian;")[0][0]
            },
            {
                "title": "Authors",
                "subtitle": "No. of available authors",
                "number": self.database.get_from_query("SELECT COUNT(*) FROM authors;")[0][0]
            },
            {
                "title": "Books",
                "subtitle": "No. of books available",
                "number": self.database.get_from_query("SELECT COUNT(*) FROM books;")[0][0]
            },
            {
                "title": "Popular",
                "subtitle": "Book with most no. of borrows",
                "number": self.database.get_from_query(
                    "SELECT COUNT(*) AS count_of_books FROM borrowed_books GROUP BY bookid ORDER BY count_of_books DESC;"
                )[0][0]
            },
            {
                "title": "Borrowed",
                "subtitle": "No. of books borrowed till date",
                "number": self.database.get_from_query("SELECT COUNT(*) FROM borrowed_books;")[0][0]
            },
            {
                "title": "Unreturned",
                "subtitle": "No. of books borrowed\nbut not returned",
                "number": self.database.get_from_query(
                    "SELECT COUNT(*) FROM borrowed_books WHERE returned!=1;"
                )[0][0]
            },
            {
                "title": "Fines",
                "subtitle": "Total fine collection till date",
                "number": self.database.get_from_query("SELECT COUNT(*) FROM transactions;")[0][0]
            },
            {
                "title": "Members",
                "subtitle": "No. of members till date",
                "number": self.database.get_from_query("SELECT COUNT(*) FROM members;")[0][0]
            },
            {
                "title": "Genres",
                "subtitle": "No. of genres",
                "number": self.database.get_from_query("SELECT COUNT(*) FROM genre;")[0][0]
            },
            {
                "title": "Positive Reviews",
                "subtitle": "No. of positive reviews",
                "number": self.database.get_from_query("SELECT COUNT(*) FROM reviews WHERE rating>7;")[0][0]
            }
        ]

    def create_frame_unit(self, title_text: str, subtitle_text: str, text: str):
        frame = CTkFrame(self, width=100, height=50, border_width=1, border_color="white", corner_radius=0)
        title = CTkLabel(
            frame,
            text=title_text,
            font=CTkFont(family="Cascadia Code", size=28, weight=NORMAL),
            text_color="white",
            fg_color="transparent"  # "#428c29"
        )
        subtitle = CTkLabel(
            frame,
            text=subtitle_text,
            font=CTkFont(family="Cascadia Code", size=14, weight=NORMAL),
            text_color="#cccccc",
            fg_color="transparent"
        )
        number = CTkLabel(frame, text=text, font=CTkFont(family="Cascadia Code", size=45, weight=BOLD))
        self.frame_list.append((frame, title, subtitle, number))

    def create_all_frames(self):
        data = self.get_data()
        for dic in data:
            self.create_frame_unit(
                title_text=dic.get("title"),
                subtitle_text=dic.get("subtitle"),
                text=str(dic.get('number'))
            )

    def create_widgets(self):
        colors = ["#428c29", "#269fa3", "#563696", "#995f25"]

        for i, (frame, title, subtitle, number) in enumerate(self.frame_list):
            frame.configure(fg_color=colors[i % 4])
            frame.grid(row=int(i / 4), column=i % 4, padx=20, pady=(40, 10), ipadx=10, ipady=10)
            title.grid(row=0, column=0, padx=10, pady=(10, 5))
            subtitle.grid(row=1, column=0, padx=10, pady=(5, 10))
            number.grid(row=0, column=1, rowspan=2, padx=10, pady=10)


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
        self.database: LibraryDB = self.controller.database
        self.container_label_text = "Library Database View"

        self.current_page = 0
        self.last_index = 49
        self.books_frame_list = []

    def get_books(self, increment=False):
        if increment:
            self.current_page += 1

        book_list = []
        results = self.database.get(table="books", columns=["*"], limit=50, offset=50 * self.current_page)
        books_table_desc = [f['Field'] for f in self.database.get_table_desc()['books']]

        for row in results:
            book_list.append({key: value for key, value in zip(books_table_desc, row)})

        return book_list

    def create_widgets(self):
        pass

    def set_scroll_bind(self):
        # self.books_frame_list[self.last_index]
        pass

    def reset(self):
        self.current_page = 0
        self.set_scroll_bind()
        self.last_index = 49
        self.books_frame_list = self.books_frame_list[:50]


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

        self.sidebar_dashboard_btn = CTkButton(self.sidebar_frame, text="Dashboard", width=200, font=CTkFont(**BUTTON_FONT), state=DISABLED, command=self.show_dashboard)
        self.sidebar_show_all_books_btn = CTkButton(self.sidebar_frame, text="Show All Books", width=200, font=CTkFont(**BUTTON_FONT), state=DISABLED, command=self.show_all_books)

        self.appearance_mode_label = CTkLabel(self.sidebar_frame, text="Appearance Mode:", anchor=N, font=CTkFont(family="Cascadia Code", weight=BOLD))
        self.appearance_mode_optionmenu = CTkOptionMenu(self.sidebar_frame, width=200,
                                                        font=CTkFont(family="Cascadia Code", weight=NORMAL),
                                                        values=["Dark", "Light", "System"],
                                                        command=self.change_appearance_mode_event)

        self.scaling_label = CTkLabel(self.sidebar_frame, text="UI Scaling:", anchor=N, font=CTkFont(family="Cascadia Code", weight=BOLD))
        self.scaling_optionmenu = CTkOptionMenu(self.sidebar_frame, width=200,
                                                font=CTkFont(family="Cascadia Code", weight=NORMAL),
                                                values=["100%", "70%", "80%", "90%", "110%", "120%", "150%"],
                                                command=self.change_scaling_event)

        self.separator_2 = CTkSeparator(self.sidebar_frame)

        self.logout_btn = CTkButton(self.sidebar_frame, text="Logout", width=200, font=CTkFont(**BUTTON_FONT), fg_color="#bd2d2d", hover_color="#821010", command=self.logout)

        self.update_idletasks()

        # ----- MAIN FRAME ------
        self.container = CTkScrollableFrame(self, label_text="Login", width=self.winfo_width(), height=self.winfo_height())
        self.current_frame = LoginFrame
        self.frames = {}
        self.frame_classes = (RegisterFrame, LoginFrame, DashboardFrame, AllBooksFrame)
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
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10), sticky=N)

        self.sidebar_insert_btn.grid(row=1, column=0, padx=20, pady=10, ipady=5, sticky=N)
        self.sidebar_update_btn.grid(row=2, column=0, padx=20, pady=10, ipady=5, sticky=N)
        self.sidebar_delete_btn.grid(row=3, column=0, padx=20, pady=10, ipady=5, sticky=N)

        self.separator_1.grid(row=4, column=0, padx=20, pady=10, sticky=EW)

        self.sidebar_dashboard_btn.grid(row=5, column=0, padx=20, pady=10, ipady=5, sticky=N)
        self.sidebar_show_all_books_btn.grid(row=6, column=0, padx=20, pady=10, ipady=5, sticky=N)

        self.appearance_mode_label.grid(row=7, column=0, padx=20, pady=(10, 0), sticky=N)
        self.appearance_mode_optionmenu.grid(row=8, column=0, padx=20, pady=(10, 10), sticky=N)
        self.scaling_label.grid(row=9, column=0, padx=20, pady=(10, 0), sticky=N)
        self.scaling_optionmenu.grid(row=10, column=0, padx=20, pady=(10, 20), sticky=N)

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
        self.sidebar_dashboard_btn.configure(state=NORMAL)
        self.sidebar_show_all_books_btn.configure(state=NORMAL)

    def add_logout_btn(self):
        self.separator_2.grid(row=11, column=0, padx=20, pady=10, sticky=EW)
        self.logout_btn.grid(row=12, column=0, padx=20, pady=(10, 20))

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

    def show_dashboard(self):
        self.remove_frame(self.current_frame)
        self.show_frame(DashboardFrame)
        self.current_frame = DashboardFrame

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
