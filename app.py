# installing flask and SQLalchemyfor use
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)



from app import db, poker_players
db.Drop_all()
db.Create_all()

 a1= poker_players(first_name='Omar',last_name='dhin',age='23', city='Bradford')
db.Session.add(a1)
db.Session.commit('this is my first entry in my database')




if __name__=='__main__':
    app.run(debug=True, host='0.0.0.0')

@app.route('/')
@app.route('/home')
def home():
    return 'This is the home page'

@app.route('/about')
def about():
    return 'This is the about page'

if __name__ == "__main__":
    app.run(debug=True)




  