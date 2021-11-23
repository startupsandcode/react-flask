from flask import Flask, request, g, jsonify
import bcrypt
from auth import bp
from api import db
from auth.models import User
from flask_httpauth import HTTPBasicAuth, HTTPTokenAuth

password_auth = HTTPBasicAuth()
token_auth = HTTPTokenAuth()

def get_hashed_password(plain_text_password):
    # Hash a password for the first time
    #   (Using bcrypt, the salt is saved into the hash itself)
    return bcrypt.hashpw(plain_text_password, bcrypt.gensalt())

def check_password(plain_text_password, hashed_password):
    # Check hashed password. Using bcrypt, the salt is saved into the hash itself
    return bcrypt.checkpw(plain_text_password, hashed_password)

@token_auth.verify_token
def verify_token(token):
    return User.verify_auth_token(token)

@password_auth.verify_password
def verify_password(username_or_token, password):
    # try to authenticate with username/password
    user = User.query.filter_by(username = username_or_token).first()
    if not user or not user.verify_password(password.encode('utf-8')):
        return False
    g.user = user
    return True

@bp.route('/login', methods=['GET', 'POST'])
def login_user():
    userdata = request.get_json()
    username = userdata['username']
    password = userdata['password'].encode('utf-8')
    user = User.query.filter_by(username=username).first()
    if user and check_password(password, user.password):
        g.user = user
        token = g.user.generate_auth_token()
        return {'success':True, 'token':token.decode('ascii')}
    return {'success':False}
    
@bp.route('/register', methods=['GET', 'POST'])
def register_user():
    userdata = request.get_json()
    username = userdata['username']
    password = userdata['password'].encode('utf-8')
    email = userdata['email']
    user = User.query.filter_by(username=username).first()
    if user:
        return {'success':False}
    hashedpassword = get_hashed_password(password)
    userdata['password'] = hashedpassword
    newUser = User(username=username, password=hashedpassword, email=email)
    db.session.add(newUser)
    db.session.commit()
    token = newUser.generate_auth_token()
    return {'success':True, 'token':token.decode('ascii')}

@bp.route('/token')
@password_auth.login_required
def get_auth_token():
    token = g.user.generate_auth_token()
    return jsonify({ 'token': token.decode('ascii') })
