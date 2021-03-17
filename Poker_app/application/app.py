# installing flask and SQLalchemyfor use
from flask import Flask, request, render_template
from flask_wtf import FlaskForm
from flask_sqlalchemy import SQLAlchemy
from models import db
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
    return render_template('home.html', title="welcome to my poker app")

@app.route('/players', methods=['GET', 'POST'])
def players():
    form = players_form
    if request.method=='POST':
        a= form.first_name.data
        b= form.last_name.data
        c= form.age.data
        d= form.city.data
    return render_template('players.html', form=form)

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

if __name__=='__main__':
    app.run(debug=True)
    



  