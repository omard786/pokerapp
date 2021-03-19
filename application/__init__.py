from flask import Flask
from flask_sqlalchemy import SQLAlchemy
template_dir="../templates"
app=Flask(__name__,template_folder=template_dir)

# #connecting to database
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:qwerty123@35.242.186.118/poker_app"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db=SQLAlchemy(app)

from application import routes