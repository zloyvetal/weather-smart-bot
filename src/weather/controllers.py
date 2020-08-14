from flask import Blueprint

w = Blueprint('weather', 'weather')


# todo: Ответ 200, название машины на котором запущено, Дебаг = тру/фолс, название сервиса

@w.route("/")
def status():
    pass


# todo: принять запрос от чатбота и отправить его в апи, потом вернуть. Валидация схемами через Педантик

@w.route("/weather")
def weather():
    pass
