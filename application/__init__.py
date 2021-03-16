#link to the databases in this app 
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = flask(__name__)
#connecting to database
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:qwerty123@35.242.186.118/poker_players"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

from application import routes

