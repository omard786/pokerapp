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

class tournements_form(FlaskForm):
    first_name = StringField('tournement_id')
    last_name = StringField('location')
    age = StringField('time starting')
    city = StringField('player_id')
    submit = SubmitField('add_tournement')

class ranking_form(FlaskForm):
    first_name = StringField('Ranking_id')
    last_name = StringField('player_id')
    age = StringField('tournement_id')
    city = StringField('prize_won')
    submit = SubmitField('add_your_rank')

   


@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/players', methods=['GET', 'POST'])
def players():
    form = players_form()
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
    form = tournements_form()
    if  request.method=='POST':
        a= request.form['tournement_id']
        b= request.form['location']
        c= request.form['timestarting']
        d= request.form['player_id']
        newtournement= poker_players(tournement_id=a, location=b, time_starting=c, player_id=d)
        db.session.add(newtournement)
        db.session.commit()
    return render_template('tournements.html', form=form)

@app.route('/rankings', methods=['GET', 'POST'])
def rankings():
    form = ranking_form()
    if request.method=='POST':
        a= request.form['Ranking_id']
        b= request.form['player_id']
        c= request.form['tournement_id']
        d= request.form['prize_won']
        newranking= poker_players(ranking_id=a, player_id=b, tournement_id=c, prize_won=d)
        db.session.add(newranking)
        db.session.commit()
    return render_template('rankings.html', form=form)


# from app import db, poker_players
# db.Drop_all()
# db.Create_all()

#  a1= poker_players(first_name='Omar',last_name='dhin',age='23', city='Bradford')
# db.Session.add(a1)
# db.Session.commit('this is my first entry in my database')

if __name__=='__main__':
    app.run(debug=True)
    



  