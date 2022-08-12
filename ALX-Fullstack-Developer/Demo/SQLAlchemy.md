# SQLAlchemy
A library in Python that can enable effective and efficient DB interaction for your app.
We will specifically look at:

How the components of SQL Alchemy and ORM are structured
What are dialects
What is a connection pool
How does the core engine work
How classes and tables are mapped
How models are defined
How data types are handled
How to define constraint

# How to use SQLAlchemy
Import the Flask-SQLAlchemy library.
Connect to our database from our Flask application
Set a configuration variable on our application by using the dictionary app.config. Flask-SQLAlchemy expects a configuration variable called, "SQLALCHEMY_DATABASE_URI".
The first parameter is our dialect of choice. In our example here, we're using postgresql (you could also use sqlite, mysql, etc).
Next is your username. (eg. postgres)
You can optionally pass in a colon password. If you have a password for your username (e.g. abc )
followed by an at sign
The name of the host location where your database is located.
For us our database server is located on our local machine. So we will just pass it in either localhost or 127.0.0.1.
Specify which port you'd like to connect to by default, 5432 for database connections.
Finally, followed by a slash and then specify the name of the particular database that exists on the server located at this host and connecting on this port, logging in with this username and password, and using this particular database system.

### Running the flask app: Terminal (option 1)
Make sure you are in the directory that contains app.py
We run a flask app defined at app.py by running this line of code on one line
```FLASK_APP=app.py FLASK_DEBUG=true flask run```
```FLASK_APP``` must be set to the server file path with an equal sign in between. No spaces. ```FLASK_APP = app.```py will not work.
```FLASK_DEBUG=true``` will enable debug mode which allows live reload
```flask run``` actually executes the flask server code in the ```app.py``` file


### Running the flask app: Python (option 2)
Make sure you are in the directory that contains app.py
Do not enter any of the flask code mentioned in option 1
Simply include the following in your python file