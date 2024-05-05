import os

from dotenv import load_dotenv
from pymysql import connect
from pymysql.connections import Connection
from pymysql.cursors import Cursor

load_dotenv('.env')
flatten = lambda t: tuple(sum(t, ()))


class LibraryDB:
    HOST: str = os.environ.get('SQL_HOST')
    USER: str = os.environ.get('SQL_USER')
    DATABASE: str = os.environ.get('SQL_DB')
    PORT: int = int(os.environ.get('SQL_PORT'))
    PASSWORD: str = os.environ.get('SQL_PASS')

    def __init__(self) -> None:
        self.engine: Connection = connect(
            host=self.HOST,
            user=self.USER,
            database=self.DATABASE,
            port=self.PORT,
            password=self.PASSWORD,
            autocommit=True
        )
        self.cursor: Cursor = self.engine.cursor()

    def get_tables(self) -> list[str]:
        self.cursor.execute("SHOW TABLES;")
        all_tables = [name[0] for name in self.cursor.fetchall()]
        return all_tables

    def get_table_desc(self) -> dict[str, list[dict[str, str]]]:
        desc_columns = ['Field', 'Type', 'Null', 'Key', 'Default', 'Extra']
        all_tables = self.get_tables()
        all_table_desc = dict()
        for table in all_tables:
            self.cursor.execute(f"DESC {table};")
            all_table_desc[table] = [
                {key: value for key, value in zip(desc_columns, row)}
                for row in (self.cursor.fetchall())
            ]
        return all_table_desc

    def get(self, table: str, columns: list[str], where: list[str] = None, limit: int = 1000, offset: int = 0):
        if '*' in columns:
            query = f"SELECT * FROM {table} "
        else:
            query = f"SELECT {','.join(columns)} FROM {table} "

        if where is not None:
            query += ' '.join(where)

        query += f' LIMIT {limit} '
        query += f'OFFSET {offset}'

        self.cursor.execute(query)
        return self.cursor.fetchall()

    def get_from_query(self, query, args=None):
        if isinstance(args, dict):
            self.cursor.execute(query, args=args)
        elif isinstance(args, tuple):
            self.cursor.execute(query, args=flatten(args))

        return self.cursor.fetchall()

    def insert(self, *args: tuple, table: str, columns: list[str] = None, where: list[str] = None):
        if columns is not None:
            query = f"INSERT INTO {table}({','.join(columns)}) VALUES "
        else:
            query = f"INSERT INTO {table} VALUES "

        cols = len(args[0])
        row_list = []
        for _ in args:
            row_list.append("(" + ",".join(["%s" for _ in range(cols)]) + ")")

        query += ','.join(row_list)

        if where is not None:
            query += ' '.join(where)

        self.cursor.execute(query, args=flatten(args))
        self.engine.commit()


if __name__ == '__main__':
    from pprint import pprint

    db = LibraryDB()
    pprint(db.get_table_desc(), indent=4, width=80, sort_dicts=False, depth=3)
    # print(db.get_from_query("SELECT * FROM genre;"))
    # db.insert(
    #     ("William Dafoe", "American"),
    #     ("Tenali Rama", "Indian"),
    #     table="authors",
    #     columns=["name", "nationality"])
    db.engine.close()
