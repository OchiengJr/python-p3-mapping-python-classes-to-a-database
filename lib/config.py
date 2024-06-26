import sqlite3
from contextlib import contextmanager

# Singleton class to handle the database connection
class DatabaseConnection:
    _instance = None

    def __new__(cls, db_name):
        if cls._instance is None:
            cls._instance = super(DatabaseConnection, cls).__new__(cls)
            cls._instance._connection = sqlite3.connect(db_name)
            cls._instance._cursor = cls._instance._connection.cursor()
        return cls._instance

    @property
    def connection(self):
        return self._connection

    @property
    def cursor(self):
        return self._cursor

    def close(self):
        if self._connection:
            self._connection.close()
            DatabaseConnection._instance = None

# Context manager for handling the connection
@contextmanager
def get_db_connection(db_name):
    db = DatabaseConnection(db_name)
    try:
        yield db.cursor
    finally:
        db.close()

# Usage
DB_NAME = 'music.db'

with get_db_connection(DB_NAME) as cursor:
    # Example query to create a table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS songs (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        album TEXT NOT NULL
    )
    ''')
    db.connection.commit()
