import sqlite3


class Database:
    def __init__(self):
        self.db = sqlite3.connect("books-collection.db")
        self.cursor = self.db.cursor()

    def create_table_books(self):
        self.cursor.execute(f"CREATE TABLE books ("
                            f"id INTEGER PRIMARY KEY,"
                            f"title varchar(250) NOT NULL UNIQUE,"
                            f"author varchar(250) NOT NULL,"
                            f"rating FLOAT NOT NULL"
                            f");")
        self.db.commit()

    def insert_default_books(self):
        self.cursor.execute(f"INSERT INTO books VALUES"
                            f"(1, 'Harry Potter', 'J. K. Rowling', '9.3'),"
                            f"(2, 'Tale of Two Cities', 'Charles Dickens', 7 );")
        self.db.commit()
