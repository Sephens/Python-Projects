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

## How to use SQLAlchemy
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
<<<<<<< HEAD
Finally, followed by a slash and then specify the name of the particular database that exists on the server located at this host and connecting on this port, logging in with this username and password, and using this particular database system.
![database-connection-uri-parts](https://user-images.githubusercontent.com/60733003/182041499-e122f18c-27db-4515-94ac-a37d91202820.png)
>>>>>>> 91bc2ccb4706e5a064c4b0e2eb30f6b4629df3f9

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
=======
Finally, followed by a slash and then specify the name of the particular database that exists on the server located at this host and connecting on this port, logging in with this username and password, and using this particular database system. See the image below:

### Takeaways
Given an instance of the SQLAlchemy class from Flask-SQLAlchemy,

db = SQLAlchemy(app)
db is an interface for interacting with our database
db.Model lets us create and manipulate data models
db.session lets us create and manipulate database transactions

### Takeaways
Declaring classes
class MyModel```(db.Model)``` will inherit from ```db.Model```
By inheriting from ```db.Model```, we map from our classes to tables via SQLAlchemy ORM
Defining columns
Within our class, we declare attributes equal to ```db.Column(...)```
db.Column takes ```<datatype>, <primary_key?>, <constraint?>, <default?>```
Table naming
By default, SQLAlchemy will pick the name of the table for you, setting it equal to the lower-case version of your class's name. Otherwise, we set the name of the table using``` __tablename__ = 'my_custom_table_name'.```

db.create_all() actually creates that tables based on the db.Model that was configured with the associated table

### SQLAlchemy Data Types
SQLAlchemy has its own data types that we should become familiar with. In SQLAlchemy, there is a one-to-one parity between an SQLAlchemy datatype and the data type that would be understandable in the semantics of the particular database system that you're linking your SQLAlchemy engine to.

db.integer, that's the integer type for the database system that we're using.
db.string, where you can optionally pass in a number that represents the maximum length of that string should be. For Postgress in particular, we're able to specify a variable character string, so we can omit the size variable, so that setting db.string with nothing in it, specifies a varchar data fields.
db.text for longer text
db.DateTime for date time objects
floats
Booleans
PickleTypes
large binaries for storing large binary data or pickled Python objects.


We generally don't need to memorize these SQLAlchemy datatypes, but keep this in mind as a reference, as you're figuring out how to define your models in your application.

Resources
Flask-SQLAlchemy: Declaring Models
See some examples including one-many and many-many relationships
Getting Started with PostgreSQL Data Types
Find out more about data types including Boolean, character, numeric, temporal, array, json, uuid, and special types.
Column and Data Types
Use the Flask-SQLAlchemy documentation site to learn about data types generally mapping to SQLAlchemy's library of data types.

![screen-shot-2019-08-18-at-11 36 57-pm](https://user-images.githubusercontent.com/60733003/184356458-6b11594f-6eaa-4eb2-860b-abaa036e702f.png)

### SQLAlchemy Constraints

Takeaways
Column constraints ensure data integrity across our database, allowing for database accuracy and consistency.
Constraints are conditions on your column, that provide checks on the data's validity. It does not allow data that violates constraints to be inserted into the database (it will raise an error if you attempt to).
In SQLAlchemy, constraints are set in ```db.Column()``` after setting the data type.
nullable=False is equivalent to ```NOT NULL``` in SQL
```unique=True``` is equivalent to ```UNIQUE``` in ```SQL```

### SUMMARY

How the components of SQL Alchemy and ORM are structured
What are dialects
What is a connection pool
How does the core engine work
How classes and tables are mapped
How models are defined
How data types are handled
How to define constraints

![sqlalchemy-layers](https://user-images.githubusercontent.com/60733003/184358136-2a642701-ae3e-45cf-bd0c-03e1460cd1a8.png)

![screen-shot-2019-08-18-at-11 58 46-pm](https://user-images.githubusercontent.com/60733003/184358228-d740a746-f6a3-443c-999d-58d85b569a64.png)


![screen-shot-2019-08-18-at-11 59 53-pm](https://user-images.githubusercontent.com/60733003/184358299-b756ca50-158d-478f-bfc6-c733cdf3ab32.png)


![screen-shot-2019-08-19-at-12 00 00-am](https://user-images.githubusercontent.com/60733003/184358382-627795a8-9103-4d0d-bd6e-db91ecc4bfe9.png)

