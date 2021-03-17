from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
class poker_players(db.Model):
    player_id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(15), nullable=False)
    last_name = db.Column(db.String(15), nullable=False)
    age = db.Column(db.String(15), nullable=False)
    city = db.Column(db.String(30), nullable=False)

class tournements(db.Model):
    tournement_id = db.Column(db.Integer, primary_key=True)
    location = db.Column(db.String(15), nullable=False)
    time_starting = db.Column(db.String(15), nullable=False)
    player_id = db.Column(db.String(15))
    
class rankings(db.Model):
    ranking_id = db.Column(db.Integer, primary_key=True)
    player_id = db.Column(db.String(15), nullable=False)
    tournement_id = db.Column(db.String(15), nullable=False)
    prize_money_won = db.Column(db.String(15), nullable=False)
    
