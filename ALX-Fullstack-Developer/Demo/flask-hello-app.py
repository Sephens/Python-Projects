import imp
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# instantiate the application
app = Flask(__name__)
# link an instance of a db that we can use in our app
db = SQLAlchemy(app)
# set a configuration variable and set it to a string that the db will understand
app.config['SQLALCHEMY_DATABASE_URI'] = ''
# enable the app to listen to the home page(the root route)
@app.route('/')
# define some methods that will act as the route handler
def index():
    return('Hello world')

# Run a flask application in terminal by:
# FLASK_APP=app_name flask run
