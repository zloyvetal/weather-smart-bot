import json

import logging

from aiogram import types
from aiogram.types import Message

from root.settings import SETTINGS
from chatbot.bot import dp, session

logging.basicConfig(level=logging.DEBUG)


@dp.message_handler(commands=['help'])
async def help_menu(message: Message):
    """Функция для предоставления пользователю информации по командам бота
        принимает сообщение от юзера, возращает текст с описанием команд"""
    await message.answer(text='''
    Команды бота, которые он способен понимать :
    /start - дает начало работы бота
    /help - вы уже ее используете  :)
    остальные в разработке
    ''')


@dp.message_handler(commands=['start'])
async def help_menu(message: Message):
    await message.answer(text="""
    Нус, начнемс!
    Этот чудо искуственный интелект может говорить вам погоду на сегодня, а так же давать небольшие подсказки :) 
    
    Скажите, в каком вы городе сейчас?:
        
    """)


def _take_data_from_api(city: str) -> json:
    """Take name of city and return json data with weather"""
    params = {'q': city, 'lang': 'ru', 'appid': SETTINGS.WEATHER_API_KEY}
    url = f"http://api.openweathermap.org/data/2.5/weather"
    response = session.get(url, params=params)

    return response.json()


def _how_to_wear(temp_min: int, temp_max: int) -> str:
    """Функция принимает минимальную и максимальную температуру воздуха на сегодняшний день и возвращает сообщение
    как одеться."""
    half_temp = (temp_max + temp_min) / 2
    if -15 > half_temp >= 0:
        return 'Температура ниже нуля, по этому одевайтесь потеплее.'

    if -15 > half_temp >= -25:
        return 'На улице зимно, советуем одеть теплые вещи.'

    if half_temp < -25:
        return 'На улице очень холодно, лучше оставайтесь дома :) если же все таки решились ' \
               'выйти на улицу - одевайте все самое теплое.'

    if 0 < half_temp <= 10:
        return 'Достаточно прохладно, если Вы останетесь в зимних вещах - жарко точно не будет :)' \
               ' если же будете использовать весенне/осенний гардироб, то есть шанс замерзнуть ближе к вечеру.'

    if 10 < half_temp <= 15:
        return 'Советуем использовать осенне/весенний гардероб.'

    if 15 < half_temp < 22:
        return 'Температура вполне подходит для летних нарядов.'

    if half_temp >= 22:
        return 'Летом можно носить что угодно :)'

    return ""


def _take_umbrella(weather: str) -> str:
    """ Функция для проверки нужен ли с собой зонт, если не нужен - возвращаем пожелание"""
    need_umbrella = ['Thunderstorm', 'Rain', 'Shower rain']

    if weather in need_umbrella:
        return 'Возьмите с собой зонт!'
    return "Продуктивного дня!"


def _pars_data_from_api(data: json) -> dict:
    """Получаем данные от функции _take_data_from_api в виде джсон словаря и возвращаем показатели погоды"""
    weather = data['weather'][0]['description']
    temp_min_today_celsius = int(data['main']['temp_min'] - 273.15)
    temp_max_today_celsius = int(data['main']['temp_max'] - 273.15)

    do_we_need_umbrella = _take_umbrella(data['weather'][0]['main'])
    how_to_wear = _how_to_wear(temp_min_today_celsius, temp_max_today_celsius)

    weather_data = {'do_we_need_umbrella': do_we_need_umbrella, "how_to_wear": how_to_wear,
                    "temp_min_today_celsius": temp_min_today_celsius,
                    "temp_max_today_celsius": temp_max_today_celsius,
                    "weather": weather}

    return weather_data


@dp.message_handler(content_types=types.ContentType.TEXT)
async def echo(message: Message):
    text = message.text

    if text and isinstance(text, str) and not text.startswith('/'):
        response = _take_data_from_api(text)
        if response['cod'] == 200:
            data_with_weather = _pars_data_from_api(response)

            temp = f"{data_with_weather['temp_min_today_celsius']} - {data_with_weather['temp_max_today_celsius']}" if \
                data_with_weather['temp_max_today_celsius'] != data_with_weather[
                    'temp_min_today_celsius'] else f"{data_with_weather['temp_max_today_celsius']}"

            await message.answer(
                f'Сегодня в городе {text} {data_with_weather["weather"]}.\n Температура в течении дня будет около {temp}'
                f' градуса по Цельсию. \n {data_with_weather["how_to_wear"]} \n {data_with_weather["do_we_need_umbrella"]}')
        else:
            await message.answer(f'К сожалению города {text} нет, проверьте правильность ввода!')

    else:
        await message.answer(f'Нет такой команды')
