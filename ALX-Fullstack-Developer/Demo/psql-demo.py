import psycopg2

# establish a connection to the database
conn = psycopg2.connect('dbname = school')
# open a cursor to perform db operations
cur = conn.cursor()
# drop table if exist to avoid error
cur.execute("DROP TABLE IF EXISTS Student;")
# create a table
cur.execute('''
CREATE TABLE Student(
    stud_id INTEGER PRIMARY KEY,
    fname VARCHAR NOT NULL,
    lname VARCHAR NOT NULL,
    DOB date NOT NULL
);

''')


# string interpolations
SQL = 'INSERT INTO Student(stud_id,fname,lname,DOB) VALUES(%(stud_id)s,%(fname)s,%(lname)s,%(DOB)s)'
data = {
    'stud_id':12,
    'fname' : "Steve",
    'lname' : 'Adenux',
    'DOB' :'5/10/199'
}

cur.execute(SQL,data)

# commit the transaction to the db
conn.commit()
# close the cursor
cur.close()
#close the transaction
conn.close()

