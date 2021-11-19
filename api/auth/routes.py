from flask import Flask, request
import bcrypt
from auth import bp

# Temporary Storage of Users
users = []

def get_hashed_password(plain_text_password):
    # Hash a password for the first time
    #   (Using bcrypt, the salt is saved into the hash itself)
    return bcrypt.hashpw(plain_text_password, bcrypt.gensalt())

def check_password(plain_text_password, hashed_password):
    # Check hashed password. Using bcrypt, the salt is saved into the hash itself
    return bcrypt.checkpw(plain_text_password, hashed_password)

@bp.route('/login', methods=['GET', 'POST'])
def login_user():
    userdata = request.get_json()
    username = userdata['username']
    password = userdata['password']
    for user in users:
        if user['username'] == username:
            if check_password(password, user['password']):
                return {'success':True}
            else:
                return {'success':False}
    hashedpassword = get_hashed_password(password)
    userdata['password'] = hashedpassword
    users.append({'username':userdata['username'], 'password':hashedpassword})
    print(users)
    return {'success':True}