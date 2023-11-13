<<<<<<< HEAD
from aiogram import Dispatcher, Bot
from decouple import config


TOKEN = config("TOKEN")
bot = Bot(token=TOKEN)
=======
from aiogram import Dispatcher, Bot
from decouple import config


TOKEN = config("TOKEN")
bot = Bot(token=TOKEN)
>>>>>>> github/master
dp = Dispatcher(bot=bot)