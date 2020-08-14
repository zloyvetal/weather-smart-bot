from aiogram import executor

from chatbot.bot import dp

if __name__ == '__main__':
    executor.start_polling(dp)
