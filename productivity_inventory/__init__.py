from flask import Flask
from .main.routes import main
from config import Config
from flask_migrate import Migrate

from flask_cors import CORS

app = Flask(__name__)
app.register_blueprint(main)

app.config.from_object(Config)