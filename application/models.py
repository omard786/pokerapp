#here is where i will put my databases, classes for your forms 

class poker_players(db.Model):
    player_id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(15), nullable=False)
    last_name = db.Column(db.String(15), nullable=False)
    age = db.Column(db.String(15), nullable=False)
    city = db.Column(db.String(30), nullable=False)

class tournements(db.Model):
    tournement_id = db.Column(db.Integer, primary_key=True)
    location = db.Column(db.String(15), nullable=False)
    time starting = db.Column(db.String(15), nullable=False)
    player_id = db.Column(db.String(15), foreignkey=False)
    
class stakers(db.Model):
    staker_id = db.Column(db.Integer, primary_key=True)
    player_id = db.Column(db.String(15), nullable=False)
    tournement_id = db.Column(db.String(15), nullable=False)
    Amount_staked = db.Column(db.String(15), nullable=False)
    

