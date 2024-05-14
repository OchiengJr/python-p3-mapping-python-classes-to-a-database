from lib.config import CURSOR, CONN
from lib.song import Song
import pytest

class TestSong:
    '''Class Song in song.py'''

    @pytest.fixture(autouse=True)
    def setup_and_teardown(self):
        '''Fixture to setup and teardown the songs table for each test.'''
        Song.drop_table()
        Song.create_table()
        yield
        Song.drop_table()

    def test_creates_songs_table(self):
        '''has classmethod "create_table()" that creates a table "songs" if table does not exist.'''
        Song.create_table()
        result = CURSOR.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='songs';").fetchone()
        assert result is not None, "Table 'songs' should exist"

    def test_initializes_with_name_and_album(self):
        '''takes a name and album as __init__ arguments and saves them as instance attributes.'''
        song = Song("Hold On", "Born to Sing")
        assert song.name == "Hold On", "Song name should be 'Hold On'"
        assert song.album == "Born to Sing", "Song album should be 'Born to Sing'"

    def test_saves_song_to_table(self):
        '''has instancemethod "save()" that saves a song to music.db.'''
        song = Song("Hold On", "Born to Sing")
        song.save()
        db_song = CURSOR.execute(
            'SELECT * FROM songs WHERE name=? AND album=?',
            ('Hold On', 'Born to Sing')
        ).fetchone()
        assert db_song is not None, "Song should be found in the database"
        assert db_song[1] == song.name, "Database song name should match"
        assert db_song[2] == song.album, "Database song album should match"

    def test_creates_and_returns_song(self):
        '''has classmethod "create()" that creates a Song instance, saves it, and returns it.'''
        song = Song.create("Hold On", "Born to Sing")
        db_song = CURSOR.execute(
            'SELECT * FROM songs WHERE name=? AND album=?',
            ('Hold On', 'Born to Sing')
        ).fetchone()
        assert db_song is not None, "Song should be found in the database"
        assert db_song[0] == song.id, "Database song id should match"
        assert db_song[1] == song.name, "Database song name should match"
        assert db_song[2] == song.album, "Database song album should match"

