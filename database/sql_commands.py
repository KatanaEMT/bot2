import sqlite3
from database import sql_queries


class Database:
    def __init__(self):
        self.connection = sqlite3.connect('bot.db')
        self.cursor = self.connection.cursor()

    def sql_create_tables(self):
        if self.connection:
            print('Database connected successfully')

        self.connection.execute(sql_queries.CREATE_USER_TABLE_QUERY)
        self.connection.execute(sql_queries.CREATE_BAN_USER_TABLE_QUERY)
        self.connection.execute(sql_queries.CREATE_USER_PROFILE_QUERY)
        self.connection.execute(sql_queries.CREATE_LIKE_TABLE_QUERY)

        self.connection.commit()

    def sql_insert_users(self, telegram_id, username, first_name, last_name):
        self.cursor.execute(
            sql_queries.INSERT_USER_QUERY,
            (None, telegram_id, username, first_name, last_name)
        )
        self.connection.commit()

    def sql_insert_ban_users(self, telegram_id):
        self.cursor.execute(
            sql_queries.INSERT_BAN_USER_QUERY,
            (None, telegram_id, 1)
        )
        self.connection.commit()

    def sql_select_ban_users(self, telegram_id):
        self.cursor.row_factory = lambda cursor, row: {
            "id": row[0],
            "telegram_id": row[1],
            "count": row[2],
        }
        return self.cursor.execute(
            sql_queries.SELECT_BAN_USER_QUERY,
            (telegram_id,)
        ).fetchone()

    def sql_update_ban_users_count(self, telegram_id):
        self.cursor.execute(
            sql_queries.UPDATE_BAN_USER_COUNT_QUERY,
            (telegram_id,)
        )
        self.connection.commit()

    def sql_insert_user_profile_register(self, telegram_id, nickname, age, sex, biography, geolocation, photo):
        self.cursor.execute(
            sql_queries.INSERT_USER_PROFILE_QUERY,
            (None, telegram_id, nickname, age, sex, biography, geolocation, photo)
        )
        self.connection.commit()

    def sql_select_users_form(self, telegram_id):
        self.cursor.row_factory = lambda cursor, row: {
            "id": row[0],
            "telegram_id": row[1],
            "nickname": row[2],
            "age": row[3],
            "sex": row[4],
            "biography": row[5],
            "geolocation": row[6],
            "photo": row[7],
        }
        return self.cursor.execute(
            sql_queries.SELECT_USER_FORM_QUERY,
            (telegram_id,)
        ).fetchone()

    def sql_select_all_users_form(self):
        self.cursor.row_factory = lambda cursor, row: {
            "id": row[0],
            "telegram_id": row[1],
            "nickname": row[2],
            "age": row[3],
            "sex": row[4],
            "biography": row[5],
            "geolocation": row[6],
            "photo": row[7],
        }
        return self.cursor.execute(
            sql_queries.SELECT_ALL_USER_PROFILE,
        ).fetchall()

    def sql_insert_like(self, owner, liker):
        self.cursor.execute(
            sql_queries.INSERT_LIKE_QUERY,
            (None, owner, liker,)
        )
        self.connection.commit()

    def sql_select_filter_users_form(self, tg_id):
        self.cursor.row_factory = lambda cursor, row: {
            "id": row[0],
            "telegram_id": row[1],
            "nickname": row[2],
            "age": row[3],
            "sex": row[4],
            "biography": row[5],
            "geolocation": row[6],
            "photo": row[7],
        }
        return self.cursor.execute(
            sql_queries.FILTER_LEFT_JOIN_USER_FORM_LIKE_QUERY,
            (tg_id, tg_id,)
        ).fetchall()
