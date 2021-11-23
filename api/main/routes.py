import time
from flask import Flask, request, jsonify, g
from main import bp
from flask_httpauth import HTTPBasicAuth
from auth.models import User

auth = HTTPBasicAuth()

@bp.route('/time')
@auth.login_required
def get_current_time():
    t = time.localtime()
    current_time = time.strftime("%H:%M:%S", t)
    return {'time':current_time}

@bp.route('/token')
@auth.login_required
def get_auth_token():
    token = g.user.generate_auth_token()
    return jsonify({ 'token': token.decode('ascii') })

@auth.verify_password
def verify_password(username_or_token, password):
    # first try to authenticate by token
    user = User.verify_auth_token(username_or_token)
    if not user:
        # try to authenticate with username/password
        user = User.query.filter_by(username = username_or_token).first()
        if not user or not user.verify_password(password.encode('utf-8')):
            return False
    g.user = user
    return True