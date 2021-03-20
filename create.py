from application import db
from application.models import poker_player, tournement, ranking

db.drop_all()
db.create_all()

Omar= poker_player(first_name='Omar', last_name= 'Dhin', age= '23', city='bradford')
Jack= poker_player(first_name='Jack', last_name= 'Dhin', age= '27', city='bristol')
Oliver= poker_player(first_name='Oliver', last_name= 'Oakley', age= '22', city='kent')
Michael= poker_player(first_name='Michael', last_name= 'Webster', age= '26', city='leeds')
Kelvin= poker_player(first_name='Kelvin', last_name= 'Bastow', age= '24', city='tamworth')
Hamza= poker_player(first_name='Hamza', last_name= 'Dhin', age='20', city= 'leeds')
Usama= poker_player(first_name='Usama', last_name ='Nasir', age='23', city='bradford')

db.session.add(Omar)
db.session.add(Jack)
db.session.add(Oliver)
db.session.add(Michael)
db.session.add(Kelvin)
db.session.add(Hamza)
db.session.add(Usama)
db.session.commit()

beginner_tourn= tournement(location= 'meeting room 1', time_starting= '14:00')
experience= tournement(location= 'meeting room 2', time_starting= '16:00')
professional_tourn= tournement(location= 'roof', time_starting= '18:00')

db.session.add(beginner_tourn)
db.session.add(intermediate_tourn)
db.session.add(professional_tourn)
db.session.commit()

one=ranking(position='1')
two=ranking(position='2')
three=ranking(position='3')
four=ranking(position='4')
five=ranking(position='5')
six=ranking(position='6')
seven=ranking(position='7')

db.session.add(one)
db.session.add(two)
db.session.add(three)
db.session.add(four)
db.session.add(five)
db.session.add(six)
db.session.add(seven)
db.session.commit()