import sqlite3

class Magazine:
    def __init__(self, name, category):
        self._name = name
        self._category = category
        self._id = None  # Initialize ID as None
        
        self._create_magazine()

    def _create_magazine(self):
        with sqlite3.connect('database.db') as conn:
            cursor = conn.cursor()
            # Insert the new magazine into the database
            cursor.execute("INSERT INTO magazines (name, category) VALUES (?, ?)", (self._name, self._category))
            self._id = cursor.lastrowid  # Get the ID of the newly created magazine
            conn.commit()

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if 2 <= len(value) <= 16 and self._name != value:
            self._name = value
            self._update_magazine_name()
        else:
            raise ValueError("Magazine name must be between 2 and 16 characters and different from the current name.")

    def _update_magazine_name(self):
        with sqlite3.connect('database.db') as conn:
            cursor = conn.cursor()
            cursor.execute("UPDATE magazines SET name = ? WHERE id = ?", (self._name, self._id))
            conn.commit()

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if len(value) > 0 and self._category != value:
            self._category = value
            self._update_magazine_category()
        else:
            raise ValueError("Category must be a non-empty string and different from the current category.")

    def _update_magazine_category(self):
        with sqlite3.connect('database.db') as conn:
            cursor = conn.cursor()
            cursor.execute("UPDATE magazines SET category = ? WHERE id = ?", (self._category, self._id))
            conn.commit()

    def articles(self):
        with sqlite3.connect('database.db') as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM articles WHERE magazine_id = ?", (self._id,))
            articles = cursor.fetchall()
        return articles or []

    def contributors(self):
        with sqlite3.connect('database.db') as conn:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT DISTINCT a.name FROM authors a
                JOIN articles ar ON ar.author_id = a.id
                WHERE ar.magazine_id = ?
            """, (self._id,))
            contributors = cursor.fetchall()
        return [contributor[0] for contributor in contributors] or []

    def article_titles(self):
        with sqlite3.connect('database.db') as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT title FROM articles WHERE magazine_id = ?", (self._id,))
            titles = cursor.fetchall()
        return [title[0] for title in titles] or []

    def contributing_authors(self):
        with sqlite3.connect('database.db') as conn:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT a.name FROM authors a
                JOIN articles ar ON ar.author_id = a.id
                WHERE ar.magazine_id = ?
                GROUP BY a.id
                HAVING COUNT(ar.id) > 2
            """, (self._id,))
            authors = cursor.fetchall()
        return [author[0] for author in authors] or []
