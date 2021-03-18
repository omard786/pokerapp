from app import db
from application.models import poker_player, tournement 
# from application import db
db.drop_all() 
db.create_all() 

Omar= poker_player(first_name='Omar', last_name= 'Dhin', age= '23', city='bradford')
Jack= poker_player(first_name='Jack', last_name= 'Dhin', age= '23', city='bristol')
Oliver= poker_player(first_name='Oliver', last_name= 'Oakley', age= '23', city='kent')
Michael= poker_player(first_name='Michael', last_name= 'Dhin', age= '23', city='leeds')
Kelvin= poker_player(first_name='Kelvin', last_name= 'Bastow', age= '26', city='london')
Hamza= poker_player(first_name='Hamza', last_name= 'younas', age='')

db.session.add(Omar)
db.session.add(Jack)
db.session.add(Oliver)
db.session.add(Michael)
db.session.add(Kelvin)
db.session.commit()

beginner_tourn= tournement(location= 'meeting room 1', time_starting= '14:00')
intermediate_tourn= tournement(location= 'meeting room 2', time_starting= '16:00')
professional_tourn= tournement(location= 'roof', time_starting= '18:00')

db.session.add(beginner_tourn)
db.session.add(intermediate_tourn)
db.session.add(professional_tourn)
db.session.commit()
