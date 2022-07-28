import psycopg2
# establish a connection to the database
conn = psycopg2.connect('dbname=example')

cursor = conn.cursor()

# Open a cursor to perform database operations
cur = conn.cursor()

# drop any existing todos table
cur.execute("DROP TABLE IF EXISTS todos;")

# (re)create the todos table
# (note: triple quotes allow multiline text in python)
cur.execute("""
  CREATE TABLE todos (
    id serial PRIMARY KEY,
    description VARCHAR NOT NULL
  );
""")

# string interpolation
cur.execute('INSERT INTO todos(id,description) VALUES(%s,%s);',(202,'Smart'))

# string interpolation example 2
SQL = "INSERT INTO todos(id,description) VALUES(%(id)s,%(description)s);"

data = {
    'id' : 2,
    'description' : 'Programming'
}
cur.execute(SQL,data)


# commit, so it does the executions on the db and persists in the db
conn.commit()

cur.close()
conn.close()