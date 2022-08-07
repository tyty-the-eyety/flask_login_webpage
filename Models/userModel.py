from functools import wraps
from flask import request, jsonify, make_response
import jwt
from config import app
from DatabaseModels.UserDB import Users
from werkzeug.security import check_password_hash
import datetime

def tokenRequired(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None

        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']

        if not token:
            return jsonify({'success': 'false', 'message': 'Token is missing'}), 401

        try:
            data = jwt.decode(token, app.config['SECRET_KEY'])
            currentUser = Users.query.filter_by(username=data['username']).first()
        except:
            return jsonify({'success': 'false', 'message': 'Token is invalid'}), 401

        return f(currentUser, *args, **kwargs)

    return decorated

def login(self):
    token = bytes
    #if not self or not self.username or not self.password:
    if not self or not self['email'] or not self['password']:
        return make_response('Could not verify',401,{'WWW-Authenticate':'Basic realm="Login Required"'})
    
    user = Users.query.filter_by(USERNAME=self['email']).first()
    
    if not user:
        return make_response('Could not verify',401,{'WWW-Authenticate':'Basic realm="Login Required"'})
    
    if check_password_hash(user.PASSWD,self['password']):
        
        #create token
        token = jwt.encode({'NAME':user.FIRSTNAME+' '+user.LASTNAME,'ID' : user.ID,'EMAIL' : user.EMAIL,'exp' : datetime.datetime.utcnow()+datetime.timedelta(minutes=540)},app.config['SECRET_KEY'])
        return jsonify({'token': token.decode('UTF-8')})