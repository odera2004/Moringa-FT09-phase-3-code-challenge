import sqlite3

class Article:
    def __init__(self, author, magazine, title):
        self._title = title
        self._author = author
        self._magazine = magazine
        self._id = None  # Initialize ID as None

        self._create_article()

    def _create_article(self):
        with sqlite3.connect('database.db') as conn:
            cursor = conn.cursor()
            # Insert the new article into the database, using author and magazine FK
            cursor.execute("INSERT INTO articles (author_id, magazine_id, title) VALUES (?, ?, ?)", 
                           (self._author.id, self._magazine.id, self._title))
            self._id = cursor.lastrowid  # Get the ID of the newly created article
            conn.commit()

    @property
    def id(self):
        return self._id

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        raise AttributeError("Title cannot be changed once set.")

    @property
    def author(self):
        return self._author

    @property
    def magazine(self):
        return self._magazine
