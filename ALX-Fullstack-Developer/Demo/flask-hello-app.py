import imp
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import false, true

# instantiate the application
app = Flask(__name__)

# enable the app to listen to the home page(the root route)
# @app.route is a Python decorator.
@app.route('/')

# define some methods that will act as the route handler
def index():
    return('Hello Steve')


# # link an instance of a db that we can use in our app
# db = SQLAlchemy(app)
# # set a configuration variable and set it to a string that the db will understand
# passw = '  x'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:%(passw)s@localhost:5432/example'

# # lets create a person class that will inherit from db.model
# class Person(db.Model):
#     __tablename__ = 'todos'
#     id = db.Column(db.Integer, primary_key = True)
#     name = db.Column(db.String(), nullable = False)


# # create a table using db.create_all() method
# #it detects the models and creates the tables for them automatially
# db.create_all()




# Run a flask application in terminal by:
# FLASK_APP=app_name flask run
