from flask import Flask,request, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from application import app
from application import db
from application.models import poker_player, tournement, ranking
from flask import render_template


#secretkey for forms
app.config['SECRET_KEY'] = 'YOUR_SECRET_KEY'

class players_form(FlaskForm):
    first_name = StringField('firstname')
    last_name = StringField('lastname')
    age = StringField('age')
    city = StringField('city')
    submit = SubmitField('add_player')

class tournements_form(FlaskForm):
    tournement_id= StringField('tournement_id')
    location = StringField('location')
    time_starting = StringField('time starting')
    player_id= StringField('player_id')
    submit = SubmitField('add_tournement')

class ranking_form(FlaskForm):
    ranking_id = StringField('Ranking_id')
    player_id= StringField('player_id')
    tournement_id = StringField('tournement_id')
    submit = SubmitField('add_your_rank')

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/player', methods=['GET', 'POST'])
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
        return render_template('player.html', form=form)


@app.route('/tournement', methods=['GET', 'POST'])
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
    return render_template('tournement.html', form=form)

@app.route('/ranking', methods=['GET', 'POST'])
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
    return render_template('ranking.html', form=form)

@app.route('/read')
def read():
    all_poker_player=poker_player.query.all()
    name_string= ""
    for item in all_poker_player:
        name_string+="<br>"+item.first_name
    return name_string


if __name__=='__main__':
    app.run(debug=True)