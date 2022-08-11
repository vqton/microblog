from flask import Flask, url_for
from config import Config

app = Flask(__name__, template_folder="../templates", static_folder="../static")
app.config.from_object(Config)
from core import routes
