import time, os, types
from flask import Flask, jsonify, g, request, abort
from flask.ext.restful import reqparse, abort, Api, Resource
from flask.ext.sqlalchemy import SQLAlchemy
from json import dumps


app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///%s/test.db' % os.path.dirname(__file__)
db = SQLAlchemy(app)

from entity import *


#
# PRINT INFO BEFORE REQUEST
#
@app.before_request
def before_request():
	g.start = time.time()
	print ( '>> -------------------------------------------------------------' )
	print ( 'Request started from IP : {}'.format(request.remote_addr) )

#
# PRINT INFO AFTER REQUEST
#
@app.teardown_request
def teardown_request(exception=None):
	diff = int((time.time() - g.start) * 1000)  # to get a time in ms
	print ( 'Total execution time : {}[ms]'.format(diff) )
	print ( '<< -------------------------------------------------------------' )



#
# TODOs
#	
TODOS = {
    'todo1': {'task': 'build an API'},
    'todo2': {'task': '?????'},
    'todo3': {'task': 'profit!'},
}


def abort_if_todo_doesnt_exist(todo_id):
    if todo_id not in TODOS:
        abort(404, message="Todo {} doesn't exist".format(todo_id))

parser = reqparse.RequestParser()
parser.add_argument('task', type=str)


# Todo
#   show a single todo item and lets you delete them
class Todo(Resource):
    def get(self, todo_id):
        abort_if_todo_doesnt_exist(todo_id)
        return TODOS[todo_id]

    def delete(self, todo_id):
        abort_if_todo_doesnt_exist(todo_id)
        del TODOS[todo_id]
        return '', 204

    def put(self, todo_id):
        args = parser.parse_args()
        task = {'task': args['task']}
        TODOS[todo_id] = task
        return task, 201


#
# Actually setup the Api resource routing here
#
api.add_resource(Todo, '/todos/<string:todo_id>')


#
# Example using only Flaks without Flask-RESTfull library
#
@app.route('/')
def index():
    return jsonify( { 'tasks': TODOS } )


#
# Wrapper object which returns JSON total number of objects plus array of objects
#
def wrapper(data):

	if data == None:
		abort(404)
		
	output = None
	if isinstance(data, types.ListType):
		output = []
		for obj in data:
			output.append(obj.to_dict())
	else:
		output = (data.to_dict())
		
	return jsonify(total = len(output), data=output)


#
# get list of Users by limit & offset
#
@app.route('/users', methods=['GET'])
def get_all_users():
	# get query parameters
	offset = request.args.get('offset')
	limit  = request.args.get('limit')
	# query database using SQLAlchemy
	users = User.query.offset(offset).limit(limit).all()
	# return object
	return wrapper( users )

#
# get User by ID
#
@app.route('/users/<int:id>', methods=['GET'])
def get_user_by_id(id):
	# query database using SQLAlchemy get user by provided id
	user = User.query.get(id)
	# return object
	return wrapper( user )


@app.route('/users', methods=['POST'])
def create_user():
	# create User object from JSON data	
	user = User(json=request.json)

	# save to DB
	#db.session.begin()
	try:
		db.session.add(user)
		db.session.commit()
	except:
		db.session.rollback()
		
	# return formated and sorted JSON object
	return json.dumps( request.json, sort_keys=True, indent=4 )


#	
# RUN
#
if __name__ == '__main__':
    app.run(debug=True)
	
	
	
