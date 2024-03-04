""" working with SQLite """

# import the database engine module
import sqlite3

# establish connection btwn a database, engine and py file
conn = sqlite3.connect("univ.db")

# establish an object that will allow execute queries to the database
cur = conn.cursor()

# manipulate database. create a table and add columns
cur.execute("CREATE TABLE Department(Deptno integer primary key not null unique, Name text)")
# create new table with a PK and Foreign Key
cur.execute("CREATE TABLE Students(Roll integer primary key not null unique, Name text, County text, Deptno integer, foreign key(Deptno) references Department(Deptno))")

# insert data in tables manually
cur.execute("INSERT INTO Department (Deptno, Name) VALUES (15, 'Arts')")

# automate insert data in tables
# get user input
deptNo = int(input("Insert Dept No.: "))
deptName = input("What is the name of the Department: ")
cur.execute(f"INSERT INTO Department (Deptno, Name) VALUES ({deptNo},'{deptName}')")


roll = int(input("Enter student roll No.: "))
name = input("Enter student name: ")
county = input("Enter County name: ")
deptCode = int(input("Enter Dept Code: "))
# using f strings
cur.execute(f"INSERT INTO Students (Roll, Name, County, Deptno) VALUES ({roll},'{name}','{county}',{deptCode})")

# check for error from manipulation
conn.commit()

# after using a resource in py, release them by closing it
cur.close()
conn.close()
