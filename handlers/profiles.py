import random
import sqlite3

import aiogram.utils.exceptions
from aiogram import types, Dispatcher
from const import USER_FORM_TEXT

from config import bot, ADMIN_ID, dp
from database.sql_commands import Database
from key_boards.inline_buttons import questionnaire_keyboard, like_dislike_keyboard
import random
import re


async def my_profile_call(call: types.CallbackQuery):
    db = Database()
    profile = db.sql_select_users_form(
        telegram_id=call.from_user.id
    )
    print(profile)
    with open(profile["photo"], 'rb') as photo:
        await bot.send_photo(
            chat_id=call.message.chat.id,
            photo=photo,
            caption=USER_FORM_TEXT.format(
                nickname=profile['nickname'],
                age=profile['age'],
                sex=profile['sex'],
                biography=profile['biography'],
                geolocation=profile['geolocation']
            )
        )


async def random_profile_call(call: types.CallbackQuery):
    print(call.message.caption)
    if call.message.caption.startswith("Hello"):
        pass
    else:
        try:
            await call.message.delete()
        except aiogram.utils.exceptions.MessageToDeleteNotFound:
            pass
    db = Database()
    profiles = db.sql_select_filter_users_form(
        tg_id=call.from_user.id
    )
    if not profiles:
        await bot.send_message(
            chat_id=call.from_user.id,
            text="Такого юзера не существует \n"
                 "или ты все пролайкал"
        )
        return
    print(profiles)
    random_profile = random.choice(profiles)
    with open(random_profile["photo"], 'rb') as photo:
        await bot.send_photo(
            chat_id=call.message.chat.id,
            photo=photo,
            caption=USER_FORM_TEXT.format(
                nickname=random_profile['nickname'],
                age=random_profile['age'],
                sex=random_profile['sex'],
                biography=random_profile['biography'],
                geolocation=random_profile['geolocation']
            ),
            reply_markup=await like_dislike_keyboard(
                owner_tg_id=random_profile["telegram_id"]
            )
        )


async def like_detect_call(call: types.CallbackQuery):
    owner = re.sub("liked_profile_", "", call.data)
    db = Database()
    try:
        db.sql_insert_like(
            owner=owner,
            liker=call.from_user.id
        )
    except sqlite3.IntegrityError:
        await bot.send_message(
            chat_id=call.from_user.id,
            text="Ты уже лайкнул"
        )
    finally:
        await call.message.delete()
        await random_profile_call(call=call)


def register_profile_handlers(dp: Dispatcher):
    dp.register_callback_query_handler(
        my_profile_call,
        lambda call: call.data == "my_profile"
    )
    dp.register_callback_query_handler(
        random_profile_call,
        lambda call: call.data == "random_profiles"
    )
    dp.register_callback_query_handler(
        like_detect_call,
        lambda call: "liked_profile_" in call.data
    )
