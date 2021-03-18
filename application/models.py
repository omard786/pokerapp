#from flask_sqlalchemy import SQLAlchemy
from app import db 

class poker_player(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(15), nullable=False)
    last_name = db.Column(db.String(15), nullable=False)
    age = db.Column(db.String(15), nullable=False)
    city = db.Column(db.String(30), nullable=False)
    tournement = db.relationship('tournement', backref = poker_player)
    players_ranking = db.relationship('ranking', backref = poker_player)

class tournement(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    location = db.Column(db.String(15), nullable=False)
    time_starting = db.Column(db.String(15), nullable=False)
    player_id = db.Column(db.Integer, db.ForeignKey('poker_player.id'))
    tournement_ranking = db.relationship('ranking', backref= tournement)
    
class ranking(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    player_id = db.Column(db.Integer, db.ForeignKey('poker_player.id'))
    tournement_id = db.Column(db.Integer, db.ForeignKey('tournement.id'))
    
    
