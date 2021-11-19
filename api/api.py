from flask import Flask, request
from config import Config
from flask_sqlalchemy import SQLAlchemy
#from auth.models import User
#from api import create_app, db

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)

from auth import bp as auth_bp
app.register_blueprint(auth_bp)

from main import bp as main_bp
app.register_blueprint(main_bp)

# @app.shell_context_processor
# def make_shell_context():
#     return {'db': db, 'User': User}