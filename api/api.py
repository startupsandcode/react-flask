from flask import Flask, request
from config import Config
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)

from auth import bp as auth_bp
app.register_blueprint(auth_bp)

from main import bp as main_bp
app.register_blueprint(main_bp)

from clock import bp as clock_bp
app.register_blueprint(clock_bp)
