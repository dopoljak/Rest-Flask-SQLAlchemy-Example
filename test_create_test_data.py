from main_app import *

status1 = Status( 'Status001' )

user1 = User( 'user11', 'password11', 'firstname11', 'lastname11', 'user11@example.com', status1 )
user2 = User( 'user22', 'password22', 'firstname22', 'lastname22', 'user22@example.com', status1 )


db.session.add(user1)
db.session.add(user2)

db.session.commit()

