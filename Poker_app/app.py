# installing flask and SQLalchemyfor use
from flask import Flask
 #render_template
#from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

@app.route('/home')
def home():
    return 'This is the home page'

@app.route('/players')
def players():
    return 'This is the players page'

@app.route('/tournements')
def tournements():
    return 'This is the tournements page'

@app.route('/rankings')
def rankings():
    return 'This is the rankings page'


# from app import db, poker_players
# db.Drop_all()
# db.Create_all()

#  a1= poker_players(first_name='Omar',last_name='dhin',age='23', city='Bradford')
# db.Session.add(a1)
# db.Session.commit('this is my first entry in my database')

#if __name__=='main':
app.run(debug=True)
    



  