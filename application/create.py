from app import db, poker_players

db.drop_all()
db.create_all()


db.session.commit()

