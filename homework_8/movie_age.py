import sqlite3
from datetime import datetime

def create_database():
    conn = sqlite3.connect("kinobaza.db")
    cursor = conn.cursor()

    # Створення таблиць
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS movies (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            release_year INTEGER NOT NULL,
            genre TEXT NOT NULL
        )
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS actors (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            birth_year INTEGER NOT NULL
        )
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS movie_cast (
            movie_id INTEGER,
            actor_id INTEGER,
            PRIMARY KEY (movie_id, actor_id),
            FOREIGN KEY (movie_id) REFERENCES movies(id) ON DELETE CASCADE,
            FOREIGN KEY (actor_id) REFERENCES actors(id) ON DELETE CASCADE
        )
    """)

    # Створення функції movie_age()
    def movie_age(year):
        return datetime.now().year - year

    conn.create_function("movie_age", 1, movie_age)
    conn.commit()
    conn.close()

create_database()
