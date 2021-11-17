import time
from flask import Flask

app = Flask(__name__)

@app.route('/api/time')
def get_current_time():
    t = time.localtime()
    current_time = time.strftime("%H:%M:%S", t)
    #current_time = datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]

    return {'time':current_time}