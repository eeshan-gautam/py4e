#import needed libraries
import json
import sqlite3

#establish cursor
conn = sqlite3.connect('rosterdb.sqlite')
cur = conn.cursor()

#create the needed tables
cur.executescript('''
DROP TABLE IF EXISTS User;
DROP TABLE IF EXISTS Member;
DROP TABLE IF EXISTS Course;

CREATE TABLE User(
id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
name TEXT UNIQUE
);

CREATE TABLE Course(
id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
title TEXT UNIQUE
);

CREATE TABLE Member(
user_id INTEGER,
course_id INTEGER,
role INTEGER,
PRIMARY KEY (user_id, course_id)
)
''')

print('*****now the database tables have been created....***')

#json-file to be opened
fname = input('Enter the file name to be opened: ')
if fname != 'roster_data.json':
    fname = 'roster_data.json'
    print('Wrong Input; OPENING defalut file now')

str_data = open(fname).read()
print('str_data:',str_data)
json_data = json.loads(str_data)
print('json_data:',json_data)

for entry in json_data:
    name = entry[0];
    title = entry[1];
    role = entry[2]
    print((name,title,role))

    cur.execute('''INSERT OR IGNORE INTO User (name)
    VALUES(?)''',(name,))
    cur.execute('SELECT id FROM User WHERE name=?',(name,))
    user_id = cur.fetchone()[0]

    cur.execute('''INSERT OR IGNORE INTO Course (title)
    VALUES(?)''',(title,))
    cur.execute('SELECT id FROM Course WHERE title=?',(title,))
    course_id = cur.fetchone()[0]

    cur.execute('''INSERT OR IGNORE INTO Member (user_id,course_id,role)
    VALUES(?,?,?)''',(user_id,course_id,role))

conn.commit()
