from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine

import sqlite3
  
conn = sqlite3.connect('sqlite.db')

app = Flask(__name__)
app.config['SECRET_KEY'] = 'my_secret_key'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + 'sqlite.db'
engine= create_engine(app.config['SQLALCHEMY_DATABASE_URI'])

# Create the SQLAlchemy db instance
db = SQLAlchemy(app)