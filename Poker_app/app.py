# installing flask and SQLalchemyfor use
from flask import Flask, request, render_template, 
#from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


@app.route('/home')
def home():
    return render_template('home.html', title="welcome to my poker app")

@app.route('/players', methods=['GET', 'POST', 'Delete'])
def players():
    return render_template('players.html')

@app.route('/tournements')
def tournements():
    return render_template('tournements.html')

@app.route('/rankings', methods=['GET'])
def rankings():
    return render_template('rankings.html')


# from app import db, poker_players
# db.Drop_all()
# db.Create_all()

#  a1= poker_players(first_name='Omar',last_name='dhin',age='23', city='Bradford')
# db.Session.add(a1)
# db.Session.commit('this is my first entry in my database')

#if __name__=='main':
app.run(debug=True)
    



  