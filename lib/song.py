from config import get_db_connection

class Song:
    def __init__(self, name, album, id=None):
        self.id = id
        self.name = name
        self.album = album

    def save(self):
        with get_db_connection() as cursor:
            cursor.execute('''
                INSERT INTO songs (name, album)
                VALUES (?, ?)
            ''', (self.name, self.album))
            self.id = cursor.lastrowid

    @classmethod
    def create_table(cls):
        with get_db_connection() as cursor:
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS songs (
                    id INTEGER PRIMARY KEY,
                    name TEXT NOT NULL,
                    album TEXT NOT NULL
                )
            ''')

    @classmethod
    def drop_table(cls):
        with get_db_connection() as cursor:
            cursor.execute('DROP TABLE IF EXISTS songs')

    @classmethod
    def create(cls, name, album):
        song = cls(name, album)
        song.save()
        return song
