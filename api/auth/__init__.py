from flask import Blueprint

bp = Blueprint('auth', __name__, url_prefix='/api')

from auth import routes
from auth.routes import token_auth, password_auth
from auth.models import User