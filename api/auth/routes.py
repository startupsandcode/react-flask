from flask import Flask, request
import bcrypt
from auth import bp
from api import db
from auth.models import User

# Temporary Storage of Users
#users = []

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
    password = userdata['password'].encode('utf-8')
    user = User.query.filter_by(username=username).first()
    if user and check_password(password, user.password.encode('utf-8')):
        return {'success':True}
    elif user and not check_password(password, user.password.encode('utf-8')):
        return {'success':False}
    hashedpassword = get_hashed_password(password)
    userdata['password'] = hashedpassword
    newUser = User(username=username, password=hashedpassword, email="test@test.com")
    db.session.add(newUser)
    db.session.commit()
    #users.append({'username':userdata['username'], 'password':hashedpassword})
    return {'success':True}