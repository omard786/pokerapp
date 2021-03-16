# installing flask and SQLalchemyfor use
from flask import Flask, render_template
from flask_sqlalchemy import SQLALchemy

app = Flask(__name__)

#connecting to database
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:qwerty123@35.242.186.118/poker_players"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLALchemy(app)

class poker_players(db.model):
    player_id = db.column(db.integer, primary_key=true)
    first_name = db.column(db.string(15), nullable=false)
    last_name = db.column(db.string(15), nullable=false)
    age = db.column(db.string(15), nullable=false)
    c = db.column(db.string(30), nullable=false)

if __name__=='__main__':
    app.run(debug==True, host='0.0.0.0')




  