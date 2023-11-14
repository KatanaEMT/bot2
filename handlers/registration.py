import sqlite3

from aiogram import types, Dispatcher
from const import USER_FORM_TEXT

from config import bot
from database.sql_commands import Database
from key_boards.inline_buttons import questionnaire_keyboard
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from config import DESTINATION


class RegistrationStates(StatesGroup):
    nickname = State()
    age = State()
    sex = State()
    biography = State()
    geolocation = State()
    photo = State()


async def registration_start(call: types.CallbackQuery):
    await bot.send_message(
        chat_id=call.from_user.id,
        text="Отправьте свой никнейм!"
    )
    await RegistrationStates.nickname.set()


async def load_nickname(message: types.Message,
                        state: FSMContext):
    async with state.proxy() as data:
        data['nickname'] = message.text
        print(data)
    await bot.send_message(
        chat_id=message.from_user.id,
        text="Сколько тебе лет?\n"
        "Используйте только цифры"
    )
    await RegistrationStates.next()


async def load_age(message: types.Message,
                   state: FSMContext):
    try:
        type(int(message.text))
    except ValueError:
        await bot.send_message(
            chat_id=message.from_user.id,
            text="Используйте только цифры!!!?\n"
                 "Регистрация начнется сначала"
        )
        await state.finish()
        return

    async with state.proxy() as data:
        data['age'] = message.text
        print(data)
    await bot.send_message(
        chat_id=message.from_user.id,
        text="Ваш пол?"
    )
    await RegistrationStates.next()


async def load_sex(message: types.Message,
                   state: FSMContext):
    async with state.proxy() as data:
        data['sex'] = message.text
        print(data)
    await bot.send_message(
        chat_id=message.from_user.id,
        text="Твоя биография?"
    )
    await RegistrationStates.next()


async def load_biography(message: types.Message,
                         state: FSMContext):
    async with state.proxy() as data:
        data['biography'] = message.text
        print(data)
    await bot.send_message(
        chat_id=message.from_user.id,
        text="Место проживания?"
    )
    await RegistrationStates.next()


async def load_geolocation(message: types.Message,
                           state: FSMContext):
    async with state.proxy() as data:
        data['geolocation'] = message.text
        print(data)
    await bot.send_message(
        chat_id=message.from_user.id,
        text="Отправьте фотографию?"
    )
    await RegistrationStates.next()


async def load_photo(message: types.Message,
                     state: FSMContext):
    dp = Database()
    path = await message.photo[-1].download(
        destination_dir=DESTINATION
    )
    print(path.name)

    async with state.proxy() as data:
        with open(path.name, 'rb') as photo:
            await bot.send_photo(
                chat_id=message.from_user.id,
                photo=photo,
                caption=USER_FORM_TEXT.format(
                    nickname=data['nickname'],
                    age=data['age'],
                    sex=data['sex'],
                    biography=data['biography'],
                    geolocation=data['geolocation']
                )
            )
            dp.sql_insert_user_profile_register(
                telegram_id=message.from_user.id,
                nickname=data['nickname'],
                age=data['age'],
                sex=data['sex'],
                biography=data['biography'],
                geolocation=data['geolocation'],
                photo=path.name
            )
        await bot.send_message(
            chat_id=message.from_user.id,
            text="Регистрация завершена （づ￣3￣）づ╭❤️～"
        )
        await state.finish()


def register_handlers(dp: Dispatcher):
    dp.register_callback_query_handler(
        registration_start,
        lambda call: call.data == "registration"
    )
    dp.register_message_handler(
        load_nickname,
        state=RegistrationStates.nickname,
        content_types=['text']
    )
    dp.register_message_handler(
        load_age,
        state=RegistrationStates.age,
        content_types=['text']
    )
    dp.register_message_handler(
        load_sex,
        state=RegistrationStates.sex,
        content_types=['text']
    )
    dp.register_message_handler(
        load_biography,
        state=RegistrationStates.biography,
        content_types=['text']
    )
    dp.register_message_handler(
        load_geolocation,
        state=RegistrationStates.geolocation,
        content_types=['text']
    )
    dp.register_message_handler(
        load_photo,
        state=RegistrationStates.photo,
        content_types=types.ContentTypes.PHOTO
    )

