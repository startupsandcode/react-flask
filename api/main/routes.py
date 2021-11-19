import time
from flask import Flask, request
from main import bp

@bp.route('/time')
def get_current_time():
    t = time.localtime()
    current_time = time.strftime("%H:%M:%S", t)
    return {'time':current_time}

