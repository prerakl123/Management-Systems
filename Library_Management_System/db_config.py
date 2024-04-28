import sqlite3 as sql
from main import LMSystem


class UserDB:
    def __init__(self, win: LMSystem):
        if win.USERNAME is None:
            if self.search_db() is None:
                win.show_frame(frame=None)
            else:
                self.connection = sql.connect('books.db')

    def check_and_create_db(self):
        pass

    def get_books(self) -> dict:
        pass

    def search_db(self) -> str:
        pass


# Database will contain:
# T1: Info about librarian(s) or others with access to library databse - name, password, picture, admin_tags
# T2: Info about
