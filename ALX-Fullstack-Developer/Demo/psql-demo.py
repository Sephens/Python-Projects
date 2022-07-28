import psycopg2

# establish a connection to the database
conn = psycopg2.connect('dbname = school')
# open a cursor to perform db operations
cur = conn.cursor()
# drop table if exist to avoid error
cur.execute("DROP TABLE IF EXISTS Student;")
cur.execute("DROP TABLE IF EXISTS Teacher;")
# create a table
cur.execute('''
CREATE TABLE Student(
    stud_id INTEGER PRIMARY KEY,
    fname VARCHAR NOT NULL,
    lname VARCHAR NOT NULL,
    DOB date NOT NULL,
    Department VARCHAR NOT NULL,
    Course VARCHAR NOT NULL,
    Date_Joined date NOT NULL
);

''')
cur.execute('''
CREATE TABLE Teacher(
    tr_id INTEGER PRIMARY KEY,
    fname VARCHAR NOT NULL,
    lname VARCHAR NOT NULL,
    DOB date NOT NULL,
    Department VARCHAR NOT NULL,
    Course VARCHAR NOT NULL
);

''')


# string interpolations
SQL1 = 'INSERT INTO Student(stud_id,fname,lname,DOB,Department,Course,Date_Joined) VALUES(%(stud_id)s,%(fname)s,%(lname)s,%(DOB)s,%(Department)s,%(Course)s,%(Date_Joined)s)'
data1 = {
    'stud_id':12,
    'fname' : "Steve",
    'lname' : 'Adenux',
    'DOB' :'5/10/1999',
    'Department' : 'SCAI',
    'Course' : 'Bsc IT',
    'Date_Joined' : '3/9/2018'
}

SQL2 = 'INSERT INTO Teacher(tr_id,fname,lname,DOB,Department,Course) VALUES(%(tr_id)s,%(fname)s,%(lname)s,%(DOB)s,%(Department)s,%(Course)s)'
data2 = {
    'tr_id':44,
    'fname' : "Tom",
    'lname' : 'Kalau',
    'DOB' :'5/10/1969',
    'Department' : 'FESS',
    'Course' : 'Bsc Education'
}

cur.execute(SQL1,data1)
cur.execute(SQL2,data2)
# fetch results from the database
cur.execute('SELECT * FROM Teacher;')
result1 = cur.fetchall()
print('Teacher table: ',result1)

cur.execute('SELECT * FROM Student;')
result2 = cur.fetchall()
print('Student table: ',result2)

# commit the transaction to the db
conn.commit()
conn.commit()
# close the cursor
cur.close()
#close the transaction
conn.close()

