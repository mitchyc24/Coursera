''' 
https://www.py4e.com/tools/sql-intro/?PHPSESSID=8bb10d02d1da0b504d13e86bd0a2dc46
'''


import json
import sqlite3

conn = sqlite3.connect("rosterdb.sqlite")
cur = conn.cursor()

script = open(r"Python_for_Everyone_Specialty\Using_Databases_with_Python\sql_create_roster.txt","r")

cur.executescript(script.read())

js = open(r"Python_for_Everyone_Specialty\Using_Databases_with_Python\roster_data.json").read()
js_data = json.loads(js)

count = 0
for entry in js_data:
    name = entry[0]
    course = entry[1]
    role = entry[2]

    cur.execute("INSERT OR IGNORE INTO User (name) VALUES (?)", (name,))
    cur.execute("SELECT id FROM User WHERE name = ?", (name,))
    user_id = cur.fetchone()[0]

    cur.execute("INSERT OR IGNORE INTO Course (title) VALUES (?)", (course,))
    cur.execute("SELECT id FROM Course WHERE title = ?", (course,))
    course_id = cur.fetchone()[0]

    cur.execute("INSERT OR REPLACE INTO Member (user_id, course_id, role) VALUES (?, ?, ?)", (user_id, course_id, role))

    conn.commit()
