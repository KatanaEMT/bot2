import sqlite3

from aiogram import types, Dispatcher
from config import bot, ADMIN_ID, dp
from database.sql_commands import Database
from key_boards.inline_buttons import questionnaire_keyboard
from aiogram.dispatcher import FSMContext


async def start_questionnaire_call(call: types.CallbackQuery):
    await bot.send_message(
        chat_id=call.from_user.id,
        text="Python or Mojo? ",
        reply_markup=await questionnaire_keyboard()
    )


async def python_call(call: types.CallbackQuery):
    await bot.send_message(
        chat_id=call.from_user.id,
        text="You are Python Developer❤️ "
    )


async def mojo_call(call: types.CallbackQuery):
    await bot.send_message(
        chat_id=call.from_user.id,
        text="You are Mojo Developer 👉"
    )


async def admin_call(call: types.Message):
    if call.from_user.id == int(ADMIN_ID):
        await bot.send_message(
            chat_id=call.from_user.id,
            text="Приветствую мастера (✿◡‿◡)"
        )
    else:
        await bot.send_message(
            chat_id=call.from_user.id,
            text="Ты не мой мастер ㆆ_ㆆ)"
        )


async def admin_questionnaire(call: types.Message):
    dp = Database()
    if call.from_user.id == int(ADMIN_ID):


def register_callback_handlers(dp: Dispatcher):
    dp.register_callback_query_handler(start_questionnaire_call,
                                       lambda call: call.data == "start_questionnaire")
    dp.register_callback_query_handler(python_call,
                                       lambda call: call.data == "python")
    dp.register_callback_query_handler(mojo_call,
                                       lambda call: call.data == "mojo")
    dp.register_message_handler(admin_call,
                                       lambda word: "id" in word.text)
