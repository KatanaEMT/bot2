import sqlite3

from aiogram import types, Dispatcher
from config import bot, ADMIN_ID, dp
from database.sql_commands import Database
from key_boards.inline_buttons import questionnaire_keyboard, save_favourite
from aiogram.dispatcher import FSMContext

from scraping.my_scraping import AnimeScraper
from scraping.news_scraper import NewsScraper


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


async def scraper_call(call: types.CallbackQuery):
    db = Database()
    scraper = NewsScraper()
    data = scraper.parse_data()
    for url in data[:4]:
        db.sql_insert_news(
            link=url
        )
    news = db.sql_select_news()
    for dat in news[:4]:
        await bot.send_message(
            chat_id=call.from_user.id,
            text=f"{scraper.PLUS_URL + dat['link']}",
            reply_markup=await save_favourite(dat["id"])

        )


async def anime_scraper_call(call: types.CallbackQuery):
    scraper = AnimeScraper()
    data = scraper.anime_parse_data()
    for url in data[:4]:
        await bot.send_message(
            chat_id=call.from_user.id,
            text=f"{url}"
        )


async def save_favourite_news(call: types.CallbackQuery):
    db = Database()
    owner_id = call.from_user.id
    news_id = int(call.data.replace("save_", ""))
    db.sql_insert_favourite_news(
        owner_id=owner_id,
        news_link=news_id
    )


async def select_favourite_news(call: types.CallbackQuery):
    db = Database()
    scraper = NewsScraper()
    data = db.sql_select_favourite_news(call.from_user.id)
    for dat in data:
        link = db.sql_select_link_news(
            news_link=dat["news_link"]
        )
        await bot.send_message(
            chat_id=call.from_user.id,
            text=f"{scraper.PLUS_URL + link['link']}",
        )


def register_callback_handlers(dp: Dispatcher):
    dp.register_callback_query_handler(start_questionnaire_call,
                                       lambda call: call.data == "start_questionnaire")
    dp.register_callback_query_handler(python_call,
                                       lambda call: call.data == "python")
    dp.register_callback_query_handler(mojo_call,
                                       lambda call: call.data == "mojo")
    dp.register_callback_query_handler(scraper_call,
                                       lambda call: call.data == "news")
    dp.register_callback_query_handler(save_favourite_news,
                                       lambda call: call.data.startswith('save_'))
    dp.register_callback_query_handler(select_favourite_news,
                                       lambda call: call.data == "favourite_news")
    dp.register_callback_query_handler(anime_scraper_call,
                                       lambda call: call.data == "anime_link")

