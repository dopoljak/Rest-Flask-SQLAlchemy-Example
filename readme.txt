install new virtual enviroment:
  >> 'virtualenv venv'

set current enviroment to active:
  >> 'venv\Scripts\activate'

install Flask to current enviroment:
  >> 'pip install Flask'
  
install Flask-RESTful to current enviroment:
  >> 'pip install Flask-RESTful'
  
install six module to current enviroment:
  >> 'pip install six'
  
install Flask-SQLAlchemy to current enviroment:
  >> 'pip install Flask-SQLAlchemy'

create new sqlite database:
  >> 'python test_create_db.py'
  
create new test data:
  >> 'python test_create_test_data.py'
  
check if data is saved to database (dump users):
  >> 'python test_list_all_data.py'
  -- id = 1, username = user11, firstname = firstname11, lastname = lastname11, email = user11@example.com, created = 2013-09-17 22:55:00, status = [id = 1, name = Status001]
  -- id = 2, username = user22, firstname = firstname22, lastname = lastname22, email = user22@example.com, created = 2013-09-17 22:55:00, status = [id = 1, name = Status001]
  

run http server:
  >> 'python main_app.py'
  
  -- * Running on http://127.0.0.1:5000/
  -- * Restarting with reloader
