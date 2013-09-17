from main_app import *

users = User.query.all()

for user in users:
	print ( user )