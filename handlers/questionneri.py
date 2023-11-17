import sqlite3

from aiogram import types, Dispatcher

from config import bot
from database.sql_commands import Database
from key_boards.inline_buttons import questionnaire_keyboard
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from config import DESTINATION


class QuestionnaireStates(StatesGroup):
    idea = State()
    problems = State()


async def questionnaire_start(call: types.CallbackQuery):
    await bot.send_message(
        chat_id=call.message.chat.id,
        text="Поделитесь своими идеями.\n"
             "Как улучшить бота!\n"
             "Или что добавить?"
    )
    await QuestionnaireStates.idea.set()


async def load_idea(message: types.Message,
                    state: FSMContext):
    async with state.proxy() as data:
        data['idea'] = message.text
        print(data)
    await bot.send_message(
        chat_id=message.chat.id,
        text="С какими проблемами вы столкнулись \n"
             "при создание бота?"
    )
    await QuestionnaireStates.next()


async def load_problems(message: types.Message,
                        state: FSMContext):
    dp = Database()
    async with state.proxy() as data:
        data['problems'] = message.text
        print(data)
    await bot.send_message(
            chat_id=message.chat.id,
            text='Спаисбо за ваше мнение\n'
                 'Опрос завершен（づ￣3￣）づ╭❤️～'
    )
    dp.sql_inserts_questionnaire_profile(
        telegram_id=message.chat.id,
        idea=data['idea'],
        problems=data['problems']
    )
    await state.finish()


def questionnaire_handlers(dp: Dispatcher):
    dp.register_callback_query_handler(
        questionnaire_start, lambda call: call.data == "questionnaire"
    )
    dp.register_message_handler(
        load_idea,
        state=QuestionnaireStates.idea,
        content_types=['text']
    )
    dp.register_message_handler(
        load_problems,
        state=QuestionnaireStates.problems,
        content_types=['text']
    )
