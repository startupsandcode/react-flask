from clock import bp
from auth import token_auth
import time

@bp.route('/clock')
@token_auth.login_required
def get_current_time():
    token_auth.current_user
    t = time.localtime()
    current_time = time.strftime("%H:%M:%S", t)
    return {'time':current_time}
