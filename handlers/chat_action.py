import datetime
import sqlite3

from aiogram import types, Dispatcher
from config import bot
from database.sql_commands import Database
from key_boards.inline_buttons import start_keyboard
from profanity_check import predict, predict_prob


async def chat_messages(message: types.Message):
    db = Database()
    print(message)
    if message.chat.id == 1691554964:
        ban_word_predict_prob = predict_prob([message.text])
        if ban_word_predict_prob > 0.1:
            await message.delete()
            user = db.sql_select_ban_users(
                telegram_id=message.from_user.id
            )
            await bot.send_message(
                chat_id=message.chat.id,
                text=f"Message: {message.from_user.id}, {message.from_user.first_name}\n"
                     f"Не матерись\n"
                     f"Если ты получишь 3 преда, то будешь заблокирован"
            )
            print(user)
            count = None
            try:
                count = user['count']
            except TypeError:
                pass
            if not user:
                await bot.send_message(
                    chat_id=message.chat.id,
                    text=f'Забанен: {message.from_user.first_name}')
                db.sql_insert_ban_users(
                    telegram_id=message.from_user.id,
                )
            elif count >= 3:
                await bot.ban_chat_member(
                    chat_id=message.chat.id,
                    user_id=message.from_user.id,
                    until_date=datetime.datetime.now() + datetime.timedelta(seconds=10)
                )
            elif user:
                db.sql_update_ban_users_count(
                    telegram_id=message.from_user.id
                )


def register_chat_action_handlers(dp: Dispatcher):
    dp.register_message_handler(chat_messages)