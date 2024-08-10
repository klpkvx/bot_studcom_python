import sqlite3 as sq
import config
import logging


class DataBase():
    def __init__(self, filename=config.FileLocation.database):
        self.filename = filename
        with sq.connect(filename) as con:
            cursor = con.cursor()
            cursor.execute('''
            CREATE TABLE IF NOT EXISTS users(
            telegram_id INTEGER PRIMARY KEY, 
            name TEXT,
            building TEXT
            )
            ''')
        logging.log(level=logging.INFO, msg=f'Successfully Connected to {filename}')

    def is_user_exists_in_database(self, cursor, tg_id: int) -> bool:
        cursor.execute('SELECT * FROM users WHERE telegram_id = ?', (str(tg_id),))
        data = cursor.fetchone()
        if data:
            return True
        else:
            return False

    def register_user_in_database_if_needed(self, tg_id: int, username: str):
        with sq.connect(self.filename) as con:
            cursor = con.cursor()
            if self.is_user_exists_in_database(cursor, tg_id):
                return
            cursor.execute(f'''
            INSERT INTO users (telegram_id, name) VALUES (?, ?)
            ''', (tg_id, username)
                           )

    def update_user_building(self, tg_id: int, building: str):
        with sq.connect(self.filename) as con:
            cursor = con.cursor()
            if not self.is_user_exists_in_database(cursor, tg_id):
                return
            cursor.execute(f'''
            UPDATE users SET building = ?
            ''',
                           (building,)
                           )

    def get_all_users_from_database(self):
        with sq.connect(self.filename) as con:
            cursor = con.cursor()
            cursor.execute(f'''
            SELECT * FROM users
            ''')
            result = cursor.fetchall()
            return result
