from  application import db

class poker_player(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(15), nullable=False)
    last_name = db.Column(db.String(15), nullable=False)
    age = db.Column(db.String(15), nullable=False)
    city = db.Column(db.String(30), nullable=False)
    tournements = db.relationship('tournement_players', backref = 'poker_player')

class tournement(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    location = db.Column(db.String(15), nullable=False)
    time_starting = db.Column(db.String(15), nullable=False)
    tournementplayers = db.relationship('tournement_players', backref = 'tournement')

    

class tournement_players(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    player_id = db.Column(db.Integer, db.ForeignKey('poker_player.id'))
    tournement_id = db.Column(db.Integer, db.ForeignKey('tournement.id'))
    
# # class registrationform(db.model):
# #     id = db.Column(db.Integer, primary_key=True)
# #     fullname= db.Column(db.String(30), nullable=False)
#     username= db.Column(db.String(30), nullable=False)