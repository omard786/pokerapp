from flask_sqlalchemy import SQLAlchemy
from flask import Flask

template_dir="../templates"
app = Flask(__name__, template_folder=template_dir)

# #connecting to database
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:qwerty123@35.242.186.118/poker_players"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
db.init_app(app)

db.create_all(app=app)

db = SQLAlchemy(app)

from application import routes

