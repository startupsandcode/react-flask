import time
from flask import Flask, request, jsonify, g
from main import bp
from flask_httpauth import HTTPBasicAuth, HTTPTokenAuth
from auth import password_auth, token_auth, User

@bp.route('/time')
@token_auth.login_required
def get_current_time():
    token_auth.current_user
    t = time.localtime()
    current_time = time.strftime("%H:%M:%S", t)
    return {'time':current_time}


