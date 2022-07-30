import imp
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# instantiate the application
app = Flask(__name__)

# enable the app to listen to the home page(the root route)
@app.route('/')
# define some methods that will act as the route handler
def index():
    return('Hello world')

# Run a flask application in terminal by:
# FLASK_APP=app_name flask run
