#!/usr/bin/python3

"""
A script that lists all states from the database hbtn_0e_0_usa.
Usage: ./list_states.py <mysql username> <mysql password> <database name>
"""

import sys
import MySQLdb

def list_states(username, password, database_name):
    try:
        db = MySQLdb.connect(user=username, passwd=password, db=database_name, host='localhost', port=3306)
        cursor = db.cursor()
        cursor.execute("SELECT * FROM states ORDER BY id ASC")
        data = cursor.fetchall()
        for row in data:
            print(row)
        cursor.close()
        db.close()
    except MySQLdb.Error as e:
        print("Error connecting to the database:", str(e))

if __name__ == '__main__':
    if len(sys.argv) != 4:
        print("Usage: ./list_states.py <mysql username> <mysql password> <database name>")
        sys.exit(1)
    
    username, password, database_name = sys.argv[1], sys.argv[2], sys.argv[3]
    list_states(username, password, database_name)
