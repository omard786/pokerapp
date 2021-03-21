from flask import Flask,request, url_for, request, redirect
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from application import app, models
from application import db
from application.models import poker_player, tournement, ranking 
from flask import render_template
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length


#secretkey for forms
app.config['SECRET_KEY'] = 'YOUR_SECRET_KEY'

class registrationform(FlaskForm):
    fullname = StringField('full name')
    username = StringField('username')# validators=[DataRequired(),min=2 max=25)
    submit = SubmitField('sign up')
   # remember = BooleanField('remember me')
# remember = 
class players_form(FlaskForm):
    first_name = StringField('firstname')
    last_name = StringField('lastname')
    age = StringField('age')
    city = StringField('city')
    submit = SubmitField('add_player')

class tournements_form(FlaskForm):
    tournement_id= StringField('tournement id')
    location = StringField('location')
    time_starting = StringField('time starting')
    player_id= StringField('player id')
    submit = SubmitField('add_tournement')

class ranking_form(FlaskForm):
    ranking_id = StringField('Ranking_id')
    name = StringField('name')
    position = StringField('position')
    player_id= StringField('player id')
    tournement_id = StringField('tournement_id')
    submit = SubmitField('add your rank')


@app.route('/', methods=[ 'GET', 'POST'])
@app.route('/home', methods=[ 'GET', 'POST'])
def home():
   return render_template('home.html')


#players
@app.route('/players', methods=['GET', 'POST']) 
#@app.route('/home', methods=['GET', 'POST'])
def players():
    error=""
    form=players_form()
    #this ensures the data from the website is transmitted to database 
    if(request.method=='POST'):
        first_name=form.fullname.data
        last_name=form.username.data
        age = form.age.data
        city = form.city.data
        #this doesnt let the fields be empty 
        if len(first_name) == 0 or len(last_name) == 0 or len(age) == 0 or len(city)== 0:
            error="please fill in all fields"
        else:
            try:
                new_player = models.poker_player(first_name=form.firstname.data, last_name=form.last_name.data, age=form.age.data, city=form.city.data)
                db.session.add(new_player)
                db.session.commit()
            except:
                error = " name taken, input something different"
    return render_template('players.html', form=form, message=error)

# #read route 
# @app.route('/showplayers')
# def showplayers():
#     all_players= models.poker_player.query.all()
#     return render_template('home.html', all_players=all_players)


# #update info route 
# @app.route('/update')

#tournements
@app.route('/tournement', methods=['GET', 'POST']) 
def tournement():
    error=""
    form=tournements_form()
    #this ensures the data from the website is transmitted to database 
    if(request.method=='POST'):
        tournement_id=form.tournement_id.data
        location=form.location.data
        time_starting = form.time_starting.data
        player_id = form.player_id.data
        #this doesnt let the fields be empty 
        if len(location) == 0 or len(time_starting) == 0 :
            error="please fill in all fields"
        try:
            new_tournement = models.tournement(tournement_id=form.tournement_id.data, location=form.location.data,
            time_starting=form.time_starting.data, player_id=form.player_id.data)
            db.session.add(new_tournement)
            db.session.commit()
        except:
            error = " name taken, input something different"
    return render_template('players.html', form=form, message=error)

#ranking

@app.route('/ranking', methods=['GET', 'POST']) 
#@app.route('/home', methods=['GET', 'POST'])
def ranking():
    error=""
    form=ranking_form()
    #this ensures the data from the website is transmitted to database 
    if(request.method=='POST'):
        ranking_id=form.ranking_id.data
        name = form.name.data
        position=form.position.data
        player_id = form.player_id.data
        tournement_id = form.tournement_id.data
        #this doesnt let the fields be empty 
        if len(name) == 0 or len(position) == 0:
            error="please fill in all fields"
        try:
                new_ranking = models.ranking(ranking_id=form.ranking_id.data, name=form.name.data,
                position=form.position.data, player_id=form.player_id.data, tournement_id=form.tournement_id.data)
                db.session.add(new_tournement)
                db.session.commit()
            
        except:
                error = " name taken, input something different"
    return render_template('players.html', form=form, message=error)

    















# @app.route('/register', methods=['GET', 'POST']) 
# def register():
#     error=""
#     form=registrationform()
#     #this ensures the data from the website is transmitted to database 
#     if(request.method=='POST'):
#         fullname=form.fullname.data
#         username=form.username.data
#         #this doesnt let the fields be empty 
#         if len(fullname) == 0 or len(username) == 0:
#             error="please enter a full name and username"
#         else:
#             try:
#                 new_player = models.poker_player(first_name=form.firstname.data, last_name=form.last_name.data, age=form.age.data, city=form.city.data)
#                 db.session.add(new_player)
#                 db.session.commit()
#                 return redirect('/home')
#             except:
#                 error = " name taken, input something different"
#             return 'you have signed up'

# return render_template ('register.html', form=form, message=error)

# @app. route('/', methods=['GET', 'POST'])
# @app.route('/home', methods=['GET', 'POST'])
# def home():









# @app.route('/tournement_enter', methods=['GET', 'POST'])
# def tournement_enter():
#     form = tournements_form()
#     if  request.method=='POST':
#         a= request.form['tournement_id']
#         b= request.form['location']
#         c= request.form['timestarting']
#         d= request.form['player_id']
#         newtournement= poker_app(tournement_id=a, location=b, time_starting=c, player_id=d)
#         db.session.add(newtournement)
#         db.session.commit()
#     return render_template('tournement.html', form=form)

# @app.route('/ranking', methods=['GET', 'POST'])
# def ranking():
#     form = ranking_form()
#     if request.method=='POST':
#         a= request.form['Ranking_id']
#         b= request.form['player_id']
#         c= request.form['tournement_id']
#         d= request.form['prize_won']
#         newranking= poker_app(ranking_id=a, player_id=b, tournement_id=c, prize_won=d)
#         db.session.add(newranking)
#         db.session.commit()
#     return render_template('ranking.html', form=form)

# @app.route('/allplayers')
# def allplayers():
#     allplayers=poker_player.query.all()
#     name_string= ""
#     for item in allplayers:
#         name_string+="<br>"+item.first_name+" "+ item.city
#     return name_string


# @app.route('/alltournements')
# def alltournements():
#     alltournements=tournement.query.all()
#     tourn_time=""
#     for item in alltournements:
#         tourn_time += "<br>"+ str(item.time_starting)+" "+item.location
#     return tourn_time , render_template('allltournements.html')

# @app.route('/rankings')
# def rankings():
#     rankings=ranking.query.all()
#     place=""
#     for item in ranking:
#         place+="<br>"+ str(item.position)
#         return place

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')