from flask import Blueprint

bp = Blueprint('clock', __name__, url_prefix='/api')

from clock import routes
