from flask import Flask, request, redirect
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from application import app, models
from application import db
from application.models import poker_player, tournement, tournement_players 
from flask import render_template, request, url_for
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
    location= StringField('location')
    time_starting= StringField('time starting')
    submit = SubmitField('add_tournement')

class addtournementplayers_form(FlaskForm):
    player_id = StringField('player_id')
    tournement_id = StringField('tournement_id')
    submit = SubmitField('add_player_tournement')
            

# class ranking_form(FlaskForm):
#     ranking_id = StringField('Ranking_id')
#     name = StringField('name')
#     position = StringField('position')
#     player_id= StringField('player id')
#     tournement_id = StringField('tournement_id')
#     submit = SubmitField('add your rank')


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
        firstname=form.first_name.data
        lastname=form.last_name.data
        age = form.age.data
        city = form.city.data
        #this doesnt let the fields be empty 
        if len(firstname) == 0 or len(lastname) == 0 or len(age) == 0 or len(city)== 0:
            error="please fill in all fields"
        else:
        
                new_player = models.poker_player(first_name=firstname, last_name=lastname, age=age, city=city)
                db.session.add(new_player)
                db.session.commit()
                #error = " name taken, input something different"
    return render_template('players.html', form=form, message=error)


@app.route('/allplayers')
def allplayers():
    allplayers=poker_player.query.all()
    name_string= ""
    for item in allplayers:
        name_string+="<br>"+item.first_name+" "+ item.city
    return name_string

@app.route('/deletefirstplayer')
def deletefirstplayer():
    message = 'you have deleted the first player in the database'
    playertodelete = poker_player.query.first()
    db.session.delete(playertodelete)
    db.session.commit()
    return message

# @app.route('/update/<int:player_id>')
# def update (firstplayername):
#     firstplayername= poker_player.query.first()
#     firstplayer.name=name
#     db.session.commit()
#     return firstplayer.name
# @app.route('/update/<int:player_id>', methods=['GET','POST'])
# def updateplayer(player_id):
#     player_to_update = models.poker_player.query.filter_by(id=player_id).first()
#     error = ""
#     form = players_form()

#     if request.method == 'POST':
#         player_to_update.first_name = form.first_name.data
#         player_to_update.last_name = form.last_name.data
#         player_to_update.age = form.age.data
#         player_to_update.city = form.city.data

#         if len(str(form.first_name.data)) == 0 or len(str(form.last_name.data)) == 0:
#             error = "Please fill in all fields"
            
#         else:
#             db.session.commit()
#             return redirect('/home')

#     else:
#         form.product_id.data = order_to_update.product_id
#         form.quantity.data = order_to_update.quantity
#         form.total_price.data = order_to_update.total_price
#         form.date_ordered.data = order_to_update.date_ordered
    
# @app.route('/update/<player>')
# def updateplayer():
#     last_player= poker_player.query.last()
#     last_player.name= player
#     db.session.commit()
#     return last_player.name








#     return render_template('players.html', form=form, message=error)
# #read route 
# @app.route('/showplayers')
# def showplayers():
#     all_players= models.poker_player.query.all()
#     return render_template('home.html', all_players=all_players)


# #update info route 
# @app.route('/update')

#tournements
@app.route('/tournements', methods=['GET', 'POST']) 
def tournements():
    error=""
    form=tournements_form()
    #this ensures the data from the website is transmitted to database 
    if(request.method=='POST'):
        location=form.location.data
        timestarting = form.time_starting.data
        #this doesnt let the fields be empty 
        if len(location) == 0 or len(timestarting) == 0 :
            error="please fill in all fields"
        else:
            new_tournement = models.tournement(location=location,
            time_starting=timestarting)
            db.session.add(new_tournement)
            db.session.commit()
        # except:
            # error = " name taken,input something different"
    return render_template('tournements.html', form=form, message=error)

#ranking



    

@app.route('/addtournementplayers', methods= ['GET', 'POST'])
def addtournementplayers():
    error=""
    form=addtournementplayers_form()
    if(request.method=='POST'):
        player_id = form.player_id.data
        tournement_id = form.tournement_id.data
        #this doesnt let the fields be empty 
        new_tournement_player = models.tournement_players( player_id=player_id, tournement_id=tournement_id)
        db.session.add(new_tournement_player)
        db.session.commit()
    return render_template('/addtournementplayers.html', form=form,)













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