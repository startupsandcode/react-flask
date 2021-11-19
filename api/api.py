import time
from flask import Flask, request

app = Flask(__name__)

from auth import bp as auth_bp
app.register_blueprint(auth_bp)

from main import bp as main_bp
app.register_blueprint(main_bp)
