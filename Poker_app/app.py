# installing flask and SQLalchemyfor use
from flask import Flask, request, render_template, url_for
from flask_wtf import FlaskForm
#fetching the models to use
from application.models import poker_player, tournement, ranking
from wtforms import StringField, SubmitField
from application import app


#database connection
# app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:qwerty123@35.242.186.118/poker_players"
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 
# db = SQLAlchemy(app)
# db.init_app(app)
# db.create_all(app=app)


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

@app.route('/read')
def read():
    all_poker_player=poker_player.query.all()
    name_string= ""
    for item in all_poker_player:
        name_string+="<br>"+item.first_name
    return name_string
    if 
    all_tournements=tournement.query.all()
    tourn_time=""
    for time_starting in tournement:
        tourn_time=+"<br>"+ item.time_starting
        return tourn_time

    # all_tournements= tournement.query.all()
    # tournement_string= ""
    # for time_starting in tournement:
    #     tournement_string=+"<br>"+ time_starting.name
    #     return tournement_string
    

#@app.route('/add')
#def add():




# from app import db, poker_players
# db.Drop_all()
# db.Create_all()

#  a1= poker_players(first_name='Omar',last_name='dhin',age='23', city='Bradford')
# db.Session.add(a1)
# db.Session.commit('this is my first entry in my database')

if __name__=='__main__':
    app.run(debug=True)
    



  