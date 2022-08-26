## Steps for getting a database-backed web application up and running
Here is an overview of the list of tasks we'll need to do for a given web app to run with a database.

1. Create a database
Using createdb in Postgres.

2. Establish a connection to the database
We can connect to a Postgres server from a Python web server using pyscopg2 with psycopg2.connect().

3. Define and create your data schema
Execute CREATE TABLE commands to create the tables and define the schema (attributes, data types, etc) that will define what data gets housed for our web app.

4. Seed the database with initial data
(Optional) Give the database some initial data, e.g. test data for doing local development.

5. Create routes and views
Create routes in our server that will serve pages (views) to the client. Write up our HTML, CSS, and Javascript in our views.

Then finally, to get our web app running,

6. Run the server
Get the web server running.

7. Deploy the server to the web.
... and that is, generally, how we would build a web application backed by a database.
