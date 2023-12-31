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
        self.connection.execute(sql_queries.CREATE_REFERRAL_TABLE_QUERY)
        self.connection.execute(sql_queries.CREATE_REFERRAL_USERS_TABLE_QUERY)
        self.connection.execute(sql_queries.CREATE_NEWS_TABLE_QUERY)
        self.connection.execute(sql_queries.CREATE_FAVOURITE_NEWS_TABLE_QUERY)


        try:
            self.connection.execute(sql_queries.ALTER_USER_TABLE)
            self.connection.execute(sql_queries.ALTER_USERV2_TABLE)
        except sqlite3.OperationalError:
            pass

        self.connection.commit()

    def sql_insert_users(self, telegram_id, username, first_name, last_name):
        try:
            self.cursor.execute(
            sql_queries.INSERT_USER_QUERY,
            (None, telegram_id, username, first_name, last_name, None, None,)
        )
        except sqlite3.IntegrityError:
            pass
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

    def sql_select_balance_count_referral(self, tg_id):
        self.cursor.row_factory = lambda cursor, row: {
            "balance": row[0],
            "count": row[1],
        }
        return self.cursor.execute(
            sql_queries.DOUBLE_SELECT_REFERRAL_USER_QUERY,
            (tg_id,)
        ).fetchone()

    def sql_update_reference_link(self, link, owner):
        self.cursor.execute(
            sql_queries.UPDATE_REFERENCE_LINK_QUERY,
            (link, owner,)
        )
        self.connection.commit()

    def sql_select_user(self, telegram_id):
        self.cursor.row_factory = lambda cursor, row: {
            "link": row[0],
        }
        return self.cursor.execute(
            sql_queries.SELECT_USER_LINK_QUERY,
            (telegram_id,)
        ).fetchone()

    def sql_select_user_by_link(self, link):
        self.cursor.row_factory = lambda cursor, row: {
            "tg_id": row[0],
        }
        return self.cursor.execute(
            sql_queries.SELECT_USER_BY_LINK_QUERY,
            (link,)
        ).fetchone()

    def sql_update_balance(self, tg_id):
        print(tg_id)
        self.cursor.execute(
            sql_queries.UPDATE_USER_BALANCE_QUERY,
            (tg_id,)
        )
        self.connection.commit()

    def sql_insert_referral(self, owner, referral):
        self.cursor.execute(
            sql_queries.INSERT_REFERRAL_QUERY,
            (None, owner, referral,)
        )
        self.connection.commit()

    def sql_insert_referral_users(self, owner, common_users, user_name, first_name):
        self.cursor.execute(
            sql_queries.INSERT_REFERRAL_USERS_QUERY,
            (None, owner, common_users, user_name, first_name)
        )
        self.connection.commit()

    def sql_select_referral_users(self, owner):
        self.cursor.row_factory = lambda cursor, row: {
            "id": row[0],
            "owner_id": row[1],
            "custom_id": row[2],
            "user_name": row[3],
            "first_name": row[4]
        }
        return self.cursor.execute(
            sql_queries.SELECT_REFERRAL_USERS_QUERY,
            (owner,)
        ).fetchall()

    def sql_select_news(self):
        self.cursor.row_factory = lambda cursor, row: {
            "id": row[0],
            "link": row[1],
        }
        return self.cursor.execute(
            sql_queries.SELECT_NEWS
        ).fetchall()

    def sql_select_favourite_news(self, owner_id):
        self.cursor.row_factory = lambda cursor, row: {
            "id": row[0],
            "owner_id": row[1],
            "news_link": row[2],
        }
        return self.cursor.execute(
            sql_queries.SELECT_FAVOURITE_NEWS,
            (owner_id,)
        ).fetchall()

    def sql_insert_news(self, link):
        self.cursor.execute(
            sql_queries.INSERT_NEWS,
            (None, link)
        )
        self.connection.commit()

    def sql_insert_favourite_news(self, owner_id, news_link):
        self.cursor.execute(
            sql_queries.INSERT_FAVOURITE_NEWS,
            (None, owner_id, news_link)
        )
        self.connection.commit()

    def sql_select_link_news(self, news_link):
        self.cursor.row_factory = lambda cursor, row: {
            "id": row[0],
            "link": row[1],
        }
        return self.cursor.execute(
            sql_queries.SELECT_LINK_NEWS,
            (news_link,)
        ).fetchone()
