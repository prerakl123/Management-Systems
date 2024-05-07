import os
from tkinter import Frame
from tkinter.constants import (
    NSEW, EW, N, NW, W,
    BOTH, X,
    DISABLED,
    END, TOP, CENTER
)
from tkinter.font import (
    BOLD,
    NORMAL,
    ITALIC
)

from PIL import Image
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
    CTkEntry,
    CTkImage
)
from db import LibraryDB
from dotenv import load_dotenv
from tkcalendar import Calendar
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
IMG_PATH = os.path.join(os.path.dirname(os.path.realpath(__file__)), "img")
# BG_IMG = CTkImage(Image.open(os.path.join(IMG_PATH, "library-img-2.jpg")))
EDIT_IMG = CTkImage(Image.open(os.path.join(IMG_PATH, "edit_logo.png")))
DELETE_IMG = CTkImage(Image.open(os.path.join(IMG_PATH, "delete_bin_logo.png")))


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
            font=CTkFont(**ENTRY_FONT)
        )
        self.password_entry.bind("<Return>", self.check_login)

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

    def check_login(self, _=None):
        global IS_LOGGED_IN

        if self.check_username_password(None):
            IS_LOGGED_IN = True
            self.controller.remove_frame(self.controller.current_frame)
            self.controller.show_frame(DashboardFrame)
            self.controller.current_frame = DashboardFrame
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
                "subtitle": "No. of available\nlibrarians",
                "number": self.database.get_from_query("SELECT COUNT(*) FROM librarian;")[0][0]
            },
            {
                "title": "Authors",
                "subtitle": "No. of available authors",
                "number": self.database.get_from_query("SELECT COUNT(*) FROM authors;")[0][0]
            },
            {
                "title": "Books",
                "subtitle": "No. of available books",
                "number": self.database.get_from_query("SELECT COUNT(*) FROM books;")[0][0]
            },
            {
                "title": "Popular",
                "subtitle": "Book with most\nno. of borrows",
                "number": self.database.get_from_query(
                    "SELECT COUNT(*) AS count_of_books FROM borrowed_books GROUP BY bookid ORDER BY count_of_books DESC;"
                )[0][0]
            },
            {
                "title": "Borrowed",
                "subtitle": "No. of books\nborrowed till date",
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
                "subtitle": "Total fine collection\ntill date",
                "number": self.database.get_from_query("SELECT SUM(fine) FROM transactions;")[0][0]
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
        frame = CTkFrame(self, width=250, height=100, border_width=1, border_color="white", corner_radius=0)
        title = CTkLabel(
            frame,
            text=title_text,
            font=CTkFont(family="Cascadia Code", size=28, weight=NORMAL),
            text_color="white",
            fg_color="transparent"  # "#428c29",
        )
        subtitle = CTkLabel(
            frame,
            text=subtitle_text,
            font=CTkFont(family="Cascadia Code", size=14, weight=NORMAL),
            text_color="#cccccc",
            fg_color="transparent"
        )
        number = CTkLabel(frame, text=text, font=CTkFont(family="Cascadia Code", size=50, weight=BOLD))
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
            frame.grid(row=int(i / 4), column=i % 4, padx=20, pady=(40, 10), ipadx=10, ipady=10, sticky=NSEW)
            title.grid(row=0, column=0, padx=10, pady=(10, 5), sticky=NSEW)
            subtitle.grid(row=1, column=0, padx=10, pady=(5, 10), sticky=NSEW)
            number.grid(row=0, column=1, rowspan=2, padx=10, pady=10, sticky=NSEW)

    def reset(self):
        del self.frame_list
        self.frame_list = []
        self.create_all_frames()
        self.create_widgets()


class AllBooksFrame(CTkFrame):
    def __init__(self, parent, controller, **kwargs):
        CTkFrame.__init__(self, parent, **kwargs)
        self.controller = controller
        self.database: LibraryDB = self.controller.database
        self.container_label_text = "Library Database View"

        self.is_edit_mode_on = False

        self.current_page = 0
        self.last_index = -1
        self.books_frame_list = []

        self.entry_grid_map = [
            {
                'row': 0,
                'column': 0,
                "columnspan": 4
            },
            {
                'row': 1,
                'column': 0
            },
            {
                'row': 2,
                'column': 0
            },
            {
                'row': 1,
                'column': 1
            },
            {
                'row': 2,
                'column': 1
            },
            {
                'row': 1,
                'column': 2
            }
        ]

        self.lbl_grid_map = [
            {
                'row': 0,
                'column': 0,
                "columnspan": 4
            },
            {
                'row': 1,
                'column': 0
            },
            {
                'row': 2,
                'column': 0
            },
            {
                'row': 1,
                'column': 1
            },
            {
                'row': 2,
                'column': 1
            },
            {
                'row': 1,
                'column': 2
            },
            {
                "row": 2,
                "column": 2
            }
        ]

        self.create_all()

    def get_books(self, increment=False) -> list[dict]:
        if increment:
            self.current_page += 1

        book_list = []
        results = self.database.get(table="books", columns=["*"], limit=50, offset=50 * self.current_page)
        books_table_desc = [f['Field'] for f in self.database.get_table_desc()['books']]

        for row in results:
            book_list.append({key: value for key, value in zip(books_table_desc, row)})

        return book_list

    def create_frame_units(self, metadata: dict):
        book_name = metadata.get('title')
        genres = []
        for g in metadata.get('genreid').rstrip(';').split(';'):
            genres.append(self.database.get(
                table="genre",
                columns=["name"],
                where=[f"id={g}"]
            )[0][0])
        author = self.database.get(
            table="authors",
            columns=["name"],
            where=[f'id="{metadata.get("authorid")}"']
        )[0][0]
        publication_year = metadata.get('publication_year')
        isbn = metadata.get('isbn')
        availability = str(metadata.get('availability'))
        borrowed_nums = str(self.database.get_from_query(
            f"SELECT COUNT(*) FROM `borrowed_books` WHERE bookid={metadata.get('id')} AND returned=0"
        )[0][0])

        frame = CTkFrame(self, width=400, height=150)
        frame.bind("<Escape>", lambda _: self.cancel_edit(_, frame))
        title_label = CTkLabel(frame, text=book_name, width=1700, text_color="#9e9515", font=CTkFont(
            family="Cascadia Code", size=24, weight=BOLD))
        author_label = CTkLabel(frame, text="Author: " + author, text_color="#2863b5", width=300, font=CTkFont(family="Cascadia Code", size=16, slant=ITALIC))
        genre_label = CTkLabel(frame, text="Genres: " + " | ".join(genres), width=300, font=CTkFont(family="Cascadia Code", size=16))
        publication_label = CTkLabel(frame, text="Publication Date: " + str(publication_year), width=300, font=CTkFont(family="Cascadia Code", size=16))
        isbn_label = CTkLabel(frame, text="ISBN: " + isbn, width=300, font=CTkFont(family="Cascadia Code", size=16, underline=True), cursor="hand2")
        isbn_label.bind("<Button-1>", lambda _: self.clipboard_append(isbn_label.cget('text')))
        availability_label = CTkLabel(frame, text="Total Copies: " + availability, width=300, text_color="#c73a3a", font=CTkFont(family="Cascadia Code", size=16))
        borrowed_label = CTkLabel(frame, text="Borrowed Copies: " + borrowed_nums, width=300, text_color="#16ba27", font=CTkFont(family="Cascadia Code", size=16))

        edit_btn = CTkButton(
            frame, image=EDIT_IMG,
            fg_color="#cccccc", hover_color="#a6a6a6",
            command=lambda: self.edit_book(frame),
            cursor='hand2', text=""
        )
        delete_btn = CTkButton(
            frame, image=DELETE_IMG,
            fg_color="#cccccc", hover_color="#a6a6a6",
            command=lambda: self.delete_book(frame),
            cursor='hand2', text=""
        )

        title_entry = CTkEntry(frame, placeholder_text="Enter book title", font=CTkFont(**ENTRY_FONT), width=900)
        author_entry = CTkEntry(frame, placeholder_text="Enter author name", font=CTkFont(**ENTRY_FONT), width=300)
        genre_entry = CTkEntry(frame, placeholder_text="Enter genre", font=CTkFont(**ENTRY_FONT), width=300)
        publ_entry = CTkEntry(frame, placeholder_text="Enter publication date (yyyy-mm-dd)", font=CTkFont(**ENTRY_FONT), width=300)
        isbn_entry = CTkEntry(frame, placeholder_text="Enter ISBN", font=CTkFont(**ENTRY_FONT), width=300)
        avail_entry = CTkEntry(frame, placeholder_text="Enter available no. of books", font=CTkFont(**ENTRY_FONT), width=300)

        title_entry.insert(0, title_label.cget('text'))
        author_entry.insert(0, author_label.cget('text').split(': ')[-1])
        genre_entry.insert(0, genre_label.cget('text').split(': ')[-1])
        publ_entry.insert(0, publication_label.cget('text').split(': ')[-1])
        isbn_entry.insert(0, isbn_label.cget('text').split(': ')[-1])
        avail_entry.insert(0, availability_label.cget('text').split(': ')[-1])

        title_entry.bind("<Return>", lambda _: self.confirm_edit(_, frame, metadata))
        author_entry.bind("<Return>", lambda _: self.confirm_edit(_, frame, metadata))
        genre_entry.bind("<Return>", lambda _: self.confirm_edit(_, frame, metadata))
        publ_entry.bind("<Return>", lambda _: self.confirm_edit(_, frame, metadata))
        isbn_entry.bind("<Return>", lambda _: self.confirm_edit(_, frame, metadata))
        avail_entry.bind("<Return>", lambda _: self.confirm_edit(_, frame, metadata))

        title_entry.bind("<Escape>", lambda _: self.cancel_edit(_, frame))
        author_entry.bind("<Escape>", lambda _: self.cancel_edit(_, frame))
        genre_entry.bind("<Escape>", lambda _: self.cancel_edit(_, frame))
        publ_entry.bind("<Escape>", lambda _: self.cancel_edit(_, frame))
        isbn_entry.bind("<Escape>", lambda _: self.cancel_edit(_, frame))
        avail_entry.bind("<Escape>", lambda _: self.cancel_edit(_, frame))

        self.books_frame_list.append((
            frame,
            title_label,
            author_label,
            genre_label,
            publication_label,
            isbn_label,
            availability_label,
            borrowed_label,

            edit_btn,
            delete_btn,

            title_entry,
            author_entry,
            genre_entry,
            publ_entry,
            isbn_entry,
            avail_entry
        ))

    def create_all(self):
        data = self.get_books()
        for metadata in data:
            self.create_frame_units(metadata)

    def create_widgets(self):
        for (frame, title, author, genre,
             publication, isbn, availability,
             borrowed, edit, delete,
             ti_en, au_en, ge_en,
             pu_en, is_en, av_en
             ) in self.books_frame_list:

            frame.pack(anchor=N, expand=True, fill=X, pady=10)
            title.grid(row=0, column=0, columnspan=4, pady=10, sticky=NSEW)
            author.grid(row=1, column=0, padx=20, pady=10, sticky=NSEW)
            genre.grid(row=2, column=0, padx=20, pady=10, sticky=NSEW)
            publication.grid(row=1, column=1, padx=20, pady=10, sticky=NSEW)
            isbn.grid(row=2, column=1, padx=20, pady=10, sticky=NSEW)
            availability.grid(row=1, column=2, padx=20, pady=10, sticky=NSEW)
            borrowed.grid(row=2, column=2, padx=20, pady=10, sticky=NSEW)

            edit.grid(row=1, column=3, padx=20, pady=10)
            delete.grid(row=2, column=3, padx=20, pady=10)

            ti_en.grid(row=0, column=0, columnspan=4, pady=10, sticky=NSEW)
            au_en.grid(row=1, column=0, padx=20, pady=10, sticky=NSEW)
            ge_en.grid(row=2, column=0, padx=20, pady=10, sticky=NSEW)
            pu_en.grid(row=1, column=1, padx=20, pady=10, sticky=NSEW)
            is_en.grid(row=2, column=1, padx=20, pady=10, sticky=NSEW)
            av_en.grid(row=1, column=2, padx=20, pady=10, sticky=NSEW)

            ti_en.grid_forget()
            au_en.grid_forget()
            ge_en.grid_forget()
            pu_en.grid_forget()
            is_en.grid_forget()
            av_en.grid_forget()

    def set_scroll_bind(self):
        self.books_frame_list[self.last_index].bind("<Visibility>", lambda _: print("Visible"))

    def reset(self):
        self.current_page = 0
        self.set_scroll_bind()
        self.last_index = 49
        self.books_frame_list = self.books_frame_list[:50]

    def switch_entry_labels(self, frame):
        if self.is_edit_mode_on:
            ind = -1
            for child in frame.winfo_children():
                if isinstance(child, CTkLabel):
                    child.grid_forget()

                if isinstance(child, CTkEntry):
                    ind += 1
                    child.grid(**self.entry_grid_map[ind], padx=20, pady=10, sticky=NSEW)
        else:
            ind = -1
            updated_entries = []
            for child in frame.winfo_children():
                if isinstance(child, CTkEntry):
                    updated_entries.append(child.get())
                    child.grid_forget()

                if isinstance(child, CTkLabel):
                    ind += 1
                    child.grid(**self.lbl_grid_map[ind], padx=20, pady=10, sticky=NSEW)
            return updated_entries

    def cancel_edit(self, _, frame):
        self.is_edit_mode_on = False
        ind = -1
        for child in frame.winfo_children():
            if isinstance(child, CTkEntry):
                child.grid_forget()

            if isinstance(child, CTkLabel):
                ind += 1
                child.grid(**self.lbl_grid_map[ind], padx=20, pady=10, sticky=NSEW)

    def edit_book(self, frame):
        if self.is_edit_mode_on:
            return
        self.is_edit_mode_on = True
        self.switch_entry_labels(frame)

    def confirm_edit(self, _, frame, metadata: dict):
        self.is_edit_mode_on = False
        updated_values = self.switch_entry_labels(frame)
        print(updated_values)
        lbl_list = []
        for child in frame.winfo_children():
            if isinstance(child, CTkLabel):
                lbl_list.append(child)

        for i in range(6):
            lbl_list[i].configure(text=updated_values[i])

        title, author, genre, pub, isbn, avail = updated_values
        try:
            author = self.database.get(table="authors", columns=["id"], where=[f'name="{author}"'])[0][0]
        except IndexError:
            self.database.insert(tuple([author]), table="authors", columns=['name'])
            author = self.database.get(table="authors", columns=['id'], where=[f'name="{author}"'])[0][0]

        gen_str = ''
        for g in genre.split('|'):
            try:
                gen_str += str(self.database.get(table='genre', columns=['id'], where=[f'name="{g.strip()}"'])[0][0])
            except IndexError:
                self.database.insert(tuple([g]), table='genre', columns=['name'])
                gen_str += str(self.database.get(table='genre', columns=['id'], where=[f'name="{g.strip()}"'])[0][0])
            gen_str += ';'

        self.database.execute_query(
            "UPDATE books SET title=" +
            f'"{title}", ' +
            f'authorid={author}, ' +
            f'genreid="{gen_str}", ' +
            f'publication_year="{pub}", ' +
            f'isbn="{isbn}", ' +
            f'availability="{avail}" ' +
            f'WHERE id={metadata["id"]};'
        )

    def delete_book(self, frame):
        frame.forget()


class AddNewBookFrame(CTkFrame):
    def __init__(self, parent, controller, **kwargs):
        CTkFrame.__init__(self, parent, **kwargs)
        self.controller = controller
        self.database: LibraryDB = self.controller.database
        self.container_label_text = "Insert"

        self.author_id = -1
        self.genre = ""
        self.shelf_id = -1

        self.heading_label = CTkLabel(self, text="Add a Book", font=CTkFont(**HEADING_FONT))
        self.frame = CTkFrame(self, width=600, height=450)

        width = 350

        self.book_title_label = CTkLabel(self.frame, width=width, text='Title', font=CTkFont(**LABEL_FONT))
        self.book_title_entry = CTkEntry(self.frame, width=width, placeholder_text="Enter book title", font=CTkFont(**ENTRY_FONT))

        self.author_label = CTkLabel(self.frame, width=width, text="Author", font=CTkFont(**LABEL_FONT))
        self.author_entry = CTkEntry(self.frame, width=width, placeholder_text="Enter author name", font=CTkFont(**ENTRY_FONT))
        self.author_optionmenu = CTkOptionMenu(
            self.frame,
            width=width,
            font=CTkFont(family="Cascadia Code", weight=NORMAL),
            values=[a[0] for a in self.database.get_from_query(
                "SELECT name FROM authors ORDER BY name ASC;"
            )],
            command=self.insert_author
        )
        self.author_entry.bind('<KeyPress>', self.update_author_optionmenu)
        self.author_entry.bind('<KeyRelease>', self.update_author_optionmenu)

        self.genre_label = CTkLabel(self.frame, width=width, text="Genre", font=CTkFont(**LABEL_FONT))
        self.genre_entry = CTkEntry(self.frame, width=width, placeholder_text="Enter genres separated by ';'", font=CTkFont(**ENTRY_FONT))

        self.publ_label = CTkLabel(self.frame, width=width, text="Publication Date", font=CTkFont(**LABEL_FONT))
        self.publ_cal = Calendar(
            self.frame,
            selectmode='day',
            font=("Cascadia Code", 12),
            showweeknumbers=False,
            cursor='hand2',
            date_pattern='yyyy-mm-dd',
            borderwidth=1,
            bordercolor='white'
        )

        self.isbn_label = CTkLabel(self.frame, width=width, text="ISBN", font=CTkFont(**LABEL_FONT))
        self.isbn_entry = CTkEntry(self.frame, width=width, placeholder_text="Enter ISBN no.", font=CTkFont(**ENTRY_FONT))

        self.avail_label = CTkLabel(self.frame, width=width, text="Availability", font=CTkFont(**LABEL_FONT))
        self.avail_entry = CTkEntry(self.frame, width=width, placeholder_text="Enter no. of available books", font=CTkFont(**ENTRY_FONT))

        self.shelf_label = CTkLabel(self.frame, width=width, text="Shelf", font=CTkFont(**LABEL_FONT))
        self.shelf_entry = CTkEntry(self.frame, width=width, placeholder_text="Enter shelf", font=CTkFont(**ENTRY_FONT))
        self.shelf_optionmenu = CTkOptionMenu(
            self.frame,
            width=width,
            font=CTkFont(family="Cascadia Code", weight=NORMAL),
            values=[s[0] for s in self.database.get_from_query(
                "SELECT location FROM shelf ORDER BY location ASC;"
            )],
            command=self.insert_shelf
        )
        self.shelf_entry.bind("<KeyPress>", self.update_shelf_optionmenu)
        self.shelf_entry.bind("<KeyRelease>", self.update_shelf_optionmenu)

        self.proceed_btn = CTkButton(self.frame, width=width, text="Add Book", font=CTkFont(**BUTTON_FONT), command=self.add_new_book)

    def create_widgets(self):
        self.heading_label.pack(side=TOP, anchor=CENTER, pady=(30, 20))
        self.frame.pack(side=TOP, anchor=CENTER, pady=(10, 20), padx=(10, 10))

        self.book_title_label.grid(row=0, column=0, padx=(30, 30), pady=(30, 5), sticky=W)
        self.book_title_entry.grid(row=1, column=0, padx=(30, 30), pady=(5, 10), ipady=5, ipadx=5)

        self.isbn_label.grid(row=0, column=1, padx=(30, 30), pady=(20, 5), sticky=W)
        self.isbn_entry.grid(row=1, column=1, padx=(30, 30), pady=(5, 10), ipady=5, ipadx=5)

        self.author_label.grid(row=2, column=0, padx=(30, 30), pady=(20, 5), sticky=W)
        self.author_entry.grid(row=3, column=0, padx=(30, 30), pady=(5, 5), ipady=5, ipadx=5)
        self.author_optionmenu.grid(row=4, column=0, padx=(30, 30), pady=(5, 10), ipady=5, ipadx=0)

        self.shelf_label.grid(row=2, column=1, padx=(30, 30), pady=(20, 5), sticky=W)
        self.shelf_entry.grid(row=3, column=1, padx=(30, 30), pady=(5, 5), ipady=5, ipadx=5)
        self.shelf_optionmenu.grid(row=4, column=1, padx=(30, 30), pady=(5, 10), ipady=5, ipadx=0)

        self.genre_label.grid(row=5, column=0, padx=(30, 30), pady=(20, 5), sticky=W)
        self.genre_entry.grid(row=6, column=0, padx=(30, 30), pady=(5, 10), ipady=5, ipadx=5)

        self.avail_label.grid(row=5, column=1, padx=(30, 30), pady=(20, 5), sticky=W)
        self.avail_entry.grid(row=6, column=1, padx=(30, 30), pady=(5, 10), ipady=5, ipadx=5)

        self.publ_label.grid(row=7, column=0, columnspan=2, padx=(30, 30), pady=(20, 5))
        self.publ_cal.grid(row=8, column=0, columnspan=2, padx=(30, 30), pady=(5, 10))

        self.proceed_btn.grid(row=9, column=0, columnspan=2, padx=(30, 30), pady=(10, 30))

    def insert_author(self, author: str):
        self.author_entry.delete(0, END)
        self.author_entry.insert(0, author)

    def insert_shelf(self, shelf: str):
        self.shelf_entry.delete(0, END)
        self.shelf_entry.insert(0, shelf)

    def update_author_optionmenu(self, _):
        authors = self.database.get_from_query(
            f'SELECT name FROM authors WHERE name LIKE "%{self.author_entry.get()}%" ORDER BY name ASC;'
        )
        self.author_optionmenu.configure(values=[a[0] for a in authors])
        self.author_optionmenu.update_idletasks()
        try:
            self.author_optionmenu.set(authors[0][0])
        except IndexError:
            self.author_optionmenu.set("")

    def update_shelf_optionmenu(self, _):
        shelves = self.database.get_from_query(
            f"SELECT location FROM shelf WHERE location LIKE \"%{self.shelf_entry.get()}%\" ORDER BY location ASC;"
        )
        self.shelf_optionmenu.configure(values=[s[0] for s in shelves])
        self.shelf_optionmenu.update_idletasks()
        try:
            self.shelf_optionmenu.set(shelves[0][0])
        except IndexError:
            self.shelf_optionmenu.set('')

    def add_new_book(self):
        title = self.book_title_entry.get()
        author = self.author_entry.get()
        genres = list(map(lambda x: x.strip(), self.genre_entry.get().split(';')))
        publ = self.publ_cal.get_date()
        isbn = self.isbn_entry.get()
        avail = self.avail_entry.get()
        shelf = self.shelf_entry.get()

        db_author = self.database.get_from_query(
            f"SELECT id, name FROM authors WHERE name=\"{author}\";"
        )
        if len(db_author) > 0:
            author = db_author[0][0]
        else:
            self.database.insert(
                (author, None),
                table="authors",
                columns=["name", "nationality"]
            )
            author = self.database.get_from_query(
                f"SELECT id FROM authors WHERE name=\"{author}\";"
            )[0]

        genre_names = []
        for g in genres:
            genr = None
            try:
                genr = self.database.get_from_query(f"SELECT id FROM genre WHERE name=\"{g}\"")[0][0]
            except IndexError:
                self.database.insert(tuple([g]), table="genre", columns=["name"])
            finally:
                if genr is None:
                    genr = self.database.get_from_query(f"SELECT id FROM genre WHERE name=\"{g}\"")[0][0]
                genre_names.append(str(genr))

        shelf = self.database.get_from_query(f"SELECT id FROM shelf WHERE location=\"{shelf}\"")

        self.database.insert(
            (title, author, ";".join(genre_names), publ, isbn, avail, shelf),
            table="books",
            columns=["title", "authorid", "genreid", "publication_year", "isbn", "availability", "shelfid"]
        )

        self.controller.remove_frame(self.controller.current_frame)
        self.controller.show_frame(AllBooksFrame)
        self.controller.current_frame = AllBooksFrame


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

        self.sidebar_insert_btn = CTkButton(self.sidebar_frame, text="Insert New Book", width=200, font=CTkFont(**BUTTON_FONT), state=DISABLED, command=self.insert_new_book)

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
        self.frame_classes = (RegisterFrame, LoginFrame, DashboardFrame, AllBooksFrame, AddNewBookFrame)
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

        self.sidebar_dashboard_btn.grid(row=1, column=0, padx=20, pady=10, ipady=5, sticky=N)
        self.sidebar_show_all_books_btn.grid(row=2, column=0, padx=20, pady=10, ipady=5, sticky=N)
        self.sidebar_insert_btn.grid(row=3, column=0, padx=20, pady=10, ipady=5, sticky=N)

        self.separator_1.grid(row=4, column=0, padx=20, pady=10, sticky=EW)

        self.appearance_mode_label.grid(row=5, column=0, padx=20, pady=(10, 0), sticky=N)
        self.appearance_mode_optionmenu.grid(row=6, column=0, padx=20, pady=(10, 10), sticky=N)
        self.scaling_label.grid(row=7, column=0, padx=20, pady=(10, 0), sticky=N)
        self.scaling_optionmenu.grid(row=8, column=0, padx=20, pady=(10, 20), sticky=N)

        self.container.grid(row=0, column=5, padx=10, pady=5, sticky=NSEW)

    @staticmethod
    def change_appearance_mode_event(new_appearance_mode: str):
        set_appearance_mode(new_appearance_mode)

    @staticmethod
    def change_scaling_event(new_scaling: str):
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
        self.sidebar_dashboard_btn.configure(state=NORMAL)
        self.sidebar_show_all_books_btn.configure(state=NORMAL)

    def add_logout_btn(self):
        self.separator_2.grid(row=9, column=0, padx=20, pady=10, sticky=EW)
        self.logout_btn.grid(row=10, column=0, padx=20, pady=(10, 20))

    def logout(self):
        global IS_LOGGED_IN
        IS_LOGGED_IN = False

        self.remove_frame(self.current_frame)
        self.show_frame(LoginFrame)
        self.current_frame = LoginFrame

        self.separator_2.grid_forget()
        self.logout_btn.grid_forget()

    def show_dashboard(self):
        self.remove_frame(self.current_frame)
        self.show_frame(DashboardFrame)
        self.frames[DashboardFrame].reset()
        self.current_frame = DashboardFrame

    def show_all_books(self):
        self.remove_frame(self.current_frame)
        self.show_frame(AllBooksFrame)
        self.current_frame = AllBooksFrame

    def insert_new_book(self):
        self.remove_frame(self.current_frame)
        self.show_frame(AddNewBookFrame)
        self.current_frame = AddNewBookFrame


if __name__ == '__main__':
    db = LibraryDB()
    app = LibraryApp(database=db)
    set_appearance_mode('dark')
    app.bind("<Escape>", lambda event: app.attributes("-fullscreen", False))
    app.bind('<F11>', lambda event: app.attributes('-fullscree', True))
    # app.attributes('-fullscreen', True)
    app.mainloop()
