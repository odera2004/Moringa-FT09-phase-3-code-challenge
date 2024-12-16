import sqlite3

class Author:
    def __init__(self, name, id=None):
        self._id = id
        self._name = name

        if self._id is None:  # Only insert if the id is not provided (new author)
            self._create_author()

    def _create_author(self):
        with sqlite3.connect('database.db') as conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO authors (name) VALUES (?)", (self._name,))
            self._id = cursor.lastrowid
            conn.commit()

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        raise AttributeError("Name cannot be changed once set.")

    def articles(self):
        with sqlite3.connect('database.db') as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM articles WHERE author_id = ?", (self._id,))
            articles = cursor.fetchall()
        return articles

    def magazines(self):
        with sqlite3.connect('database.db') as conn:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT DISTINCT m.name FROM magazines m
                JOIN articles a ON a.magazine_id = m.id
                WHERE a.author_id = ?
            """, (self._id,))
            magazines = cursor.fetchall()
        return magazines
