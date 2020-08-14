from flask import Flask

from weather.controllers import w

app = Flask(__name__)
app.register_blueprint(w, url_prefix="/")
