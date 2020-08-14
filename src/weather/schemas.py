import typing as t
from datetime import datetime

from pydantic import BaseModel


class UserRequest(BaseModel):
    city: str
    lang: str = 'ru'


# todo: ДОПИСАТЬ СХЕМЫ ДЛЯ ВАЛИДАЦИИ ДАННЫХ !!!



class WeatherResponse(BaseModel):
    pass


class UserResponse(BaseModel):
    pass