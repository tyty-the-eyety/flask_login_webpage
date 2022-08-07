from config import db

class Users(db.Model):
    ID = db.Column(db.Integer,primary_key=True)
    USERNAME = db.Column(db.String(50),unique=True)
    FIRSTNAME = db.Column(db.String(50))
    LASTNAME = db.Column(db.String(50))
    PASSWD = db.Column(db.String(80))
    EMAIL = db.Column(db.String(50))
    
    def __repr__(self):
        return '<User {}>'.format(self.username)  