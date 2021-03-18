#from flask_sqlalchemy import SQLAlchemy
from app import db 

class poker_player(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(15), nullable=False)
    last_name = db.Column(db.String(15), nullable=False)
    age = db.Column(db.String(15), nullable=False)
    city = db.Column(db.String(30), nullable=False)
    tournement = db.relationship('tournement', backref = 'poker_player')
    players_ranking = db.relationship('ranking', backref = 'poker_player')

all_poker_player=poker_player.query.all
all_poker_playerid=poker_player.id
poker_player_order=poker_player.order_by(poker_player.first_name).all()

#give total number of players as a interger
number_of_players=poker_player.count()



class tournement(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    location = db.Column(db.String(15), nullable=False)
    time_starting = db.Column(db.String(15), nullable=False)
    player_id = db.Column(db.Integer, db.ForeignKey('poker_player.id'))
    tournement_ranking = db.relationship('ranking', backref= 'tournement')

all_tournements=tournement.query.all
all_tournementid=tournement.id
tournement_order=poker_player.order_by(tournement.time_starting).all()

    
class ranking(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    player_id = db.Column(db.Integer, db.ForeignKey('poker_player.id'))
    tournement_id = db.Column(db.Integer, db.ForeignKey('tournement.id'))
    
all_rankings=ranking.query.all

