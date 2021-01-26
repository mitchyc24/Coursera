'''
Welcome Mitchell Carroll from Using Databases with Python

To get credit for this assignment, perform the instructions below and upload your SQLite3 database here:
(Must have a .sqlite suffix)
Hint: The top organizational count is 536.
You do not need to export or convert the database - simply upload the .sqlite file that your program creates. See the example code for the use of the connect() statement.

Counting Organizations
This application will read the mailbox data (mbox.txt) and count the number of org messages per organization (i.e. domain name of the org address) using a database with the following schema to maintain the counts.

CREATE TABLE Counts (org TEXT, count INTEGER)
When you have run the program on mbox.txt upload the resulting database file above for grading.
If you run the program multiple times in testing or with dfferent files, make sure to empty out the data before each run.

You can use this code as a starting point for your application: http://www.py4e.com/code3/orgdb.py.

The data file for this application is the same as in previous assignments: http://www.py4e.com/code3/mbox.txt.

Because the sample code is using an UPDATE statement and committing the results to the database as each record is read in the loop, it might take as long as a few minutes to process all the data. The commit insists on completely writing all the data to disk every time it is called.

The program can be speeded up greatly by moving the commit operation outside of the loop. In any database program, there is a balance between the number of operations you execute between commits and the importance of not losing the results of operations that have not yet been committed.
'''

import os
import re
import sqlite3

dest = r"Python_for_Everyone_Specialty\Using_Databases_with_Python"
inbox = r"Python_for_Everyone_Specialty\Using_Databases_with_Python\mbox.txt"
short_inbox = r"Python_for_Everyone_Specialty\Using_Databases_with_Python\mbox-short.txt"
domain_pattern = r"From: .+@([\S]+)"

def main():
    orgs = find_matches(inbox,domain_pattern)
    cursor = connect_db(os.path.join(dest,"org_set.sqlite"))
    create_counts_table(cursor)

    for org in orgs:
        update_count(cursor, org)
    cursor.connection.commit()

    verify(cursor)
    cursor.close()

    

def find_matches(f,p):
    return re.findall(domain_pattern,open(f,"r").read())

def connect_db(db):
    """ create a database connection to a SQLite database """
    try:
        print("...Connecting to", db, "SQLite3 version", sqlite3.version +"\n")
        return sqlite3.connect(db).cursor()
    except:
        print("An error has occured!")

def create_counts_table(cursor):
    cursor.execute('DROP TABLE IF EXISTS Counts')
    cursor.execute("CREATE TABLE Counts (org TEXT, count INTEGER)")

def update_count(cursor, org):
    cursor.execute('SELECT count FROM Counts WHERE org = ? ', (org,))
    row = cursor.fetchone()
    if row is None:
        cursor.execute("INSERT INTO Counts (org, count) VALUES (?, 1)", (org,))
    else:
        cursor.execute("UPDATE Counts SET count = count + 1 WHERE org = ?", (org,))


def verify(cursor):
    sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10'

    for row in cursor.execute(sqlstr):
        print(str(row[0]), row[1])


if __name__ == "__main__":
    main()