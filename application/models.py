#here is where i will put my databases, classes for your forms 
from app import db, poker_players
db.drop_all()
db.create_all()

a1 = poker_players(first_name='Omar',last_name='dhin',age='23', city='Bradford')
db.session.add(a1)
db.session.commit('this is my first entry in my database')


