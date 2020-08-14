import typing as t
from datetime import datetime

from pydantic import BaseModel


class UserRequest(BaseModel):
    city: str
    lang: str = 'ru'


# todo: ДОПИСАТЬ СХЕМЫ ДЛЯ ВАЛИДАЦИИ ДАННЫХ !!!
# fixme: FOR TEST


class WeatherResponse(BaseModel):
    id: int
    name = 'John Doe'
    signup_ts: t.Optional[datetime] = None
    friends: t.List[int] = []


class UserResponse(BaseModel):
    id: int
    name = 'John Doe'
    signup_ts: t.Optional[datetime] = None
    friends: t.List[int] = []
