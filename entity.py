from main_app import db
import datetime, json
import json, sqlalchemy
from collections import OrderedDict

#
# Helper method sqlalchemy object to dictionary
#
def model_to_dict(obj):
	dict = {}
	for c in obj.__table__.columns:
		if isinstance(c.type, sqlalchemy.DateTime):
			value = getattr(obj, c.name).strftime("%Y-%m-%d %H:%M:%S")
		else:
			value = getattr(obj, c.name)
		dict[c.name] = value
	return dict

#
# Helper json data to sqlachemy object
#
def json_to_model(obj, json):
	if json != None:
		for c in json:
			setattr(obj, c, json[c])


class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(80), unique=False)
	password = db.Column(db.String(80), unique=False)
	firstname = db.Column(db.String(80), unique=False, default=None)
	lastname = db.Column(db.String(80), unique=False, default=None)
	email = db.Column(db.String(120), unique=False, default=None)
	created = db.Column(db.DateTime, default=db.func.now())
	status_id = db.Column(db.Integer, db.ForeignKey('status.id'))
	status = db.relationship('Status', backref=db.backref('users', lazy='dynamic'))

	def __init__(self, username=None, password=None, firstname=None, lastname=None, email=None, status=None, json=None):
		self.username = username
		self.password = password
		self.firstname = firstname
		self.lastname = lastname
		self.email = email
		self.status = status
		json_to_model(self, json)

	def __repr__(self):
		return 'id = {}, username = {}, firstname = {}, lastname = {}, email = {}, created = {}, status = [{}]'.format(self.id, self.username, self.firstname, self.lastname, self.email, self.created, self.status)

	def to_dict(self):
		return model_to_dict(self)


class Status(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return 'id = {}, name = {}'.format(self.id, self.name)

	def as_dict(self):
		return model_to_dict(self)
	
