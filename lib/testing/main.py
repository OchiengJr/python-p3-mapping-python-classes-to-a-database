#!/usr/bin/env python3

from config import get_db_connection
from song import Song

def setup_database():
    Song.drop_table()
    Song.create_table()

def main():
    setup_database()
    # Example operations
    song = Song.create("Hold On", "Born to Sing")
    print(f"Created song: {song}")

if __name__ == '__main__':
    import ipdb; ipdb.set_trace()
    main()
