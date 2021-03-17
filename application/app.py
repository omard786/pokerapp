# installing flask and SQLalchemyfor use
from flask import Flask, request, render_template
from flask_wtf import FlaskForm
from flask_sqlalchemy import SQLAlchemy
from models import db, poker_players
from wtforms import StringField, SubmitField

app = Flask(__name__)
#database connection
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:qwerty123@35.242.186.118/poker_players"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 
db.init_app(app)
db.create_all(app=app)

class players_form(FlaskForm):
    first_name = StringField('firstname')
    last_name = StringField('lastname')
    age = StringField('age')
    city = StringField('city')
    submit = SubmitField('add_player')

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/players', methods=['GET', 'POST'])
def players():
    form = players_form
    if request.method=='POST':
        a= request.form['firstname']
        b= request.form['lastname']
        c= request.form['age']
        d= request.form['city']
        newplayer= poker_players(first_name=a, last_name=b, age=c, city=d)
        db.session.add(newplayer)
        db.session.commit()
    return render_template('players.html', form=form)



@app.route('/tournements', methods=['GET', 'POST'])
def tournements():
     form = tournements__form
    if  request.method=='POST':
        a= request.form['tournement_id']
        b= request.form['location']
        c= request.form['timestarting']
        d= request.form['player_id']
        newtournement= tournements(tournement_id=a, location=b, time_starting=c, player_id=d)
        db.session.add(newtournement)
        db.session.commit()
    return render_template('tournements.html')

@app.route('/rankings', methods=['GET', 'POST'])
def rankings():
     form = players_form
    if request.method=='POST':
        a= request.form['Ranking_id']
        b= request.form['player_id']
        c= request.form['tournement_id']
        d= request.form['prize_won']
        newranking= poker_players(ranking_id=a, player_id=b, tournement_id=c, prize_won=d)
        db.session.add(newpranking)
        db.session.commit()
    return render_template('rankings.html')


# from app import db, poker_players
# db.Drop_all()
# db.Create_all()

#  a1= poker_players(first_name='Omar',last_name='dhin',age='23', city='Bradford')
# db.Session.add(a1)
# db.Session.commit('this is my first entry in my database')

if __name__=='__main__':
    app.run(debug=True)
    



  