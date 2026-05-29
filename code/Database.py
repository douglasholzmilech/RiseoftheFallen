import sqlite3


class Database:

    @staticmethod
    def connect():

        conn = sqlite3.connect('score.db')

        cursor = conn.cursor()

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS score (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                points INTEGER
            )
        ''')

        conn.commit()

        return conn