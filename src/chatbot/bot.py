from aiogram import Dispatcher, Bot
from requests import Session
from root.settings import SETTINGS

bot = Bot(SETTINGS.BOT_TOKEN, parse_mode='HTML')
dp = Dispatcher(bot)


session = Session()

