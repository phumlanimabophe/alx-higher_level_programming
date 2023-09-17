#!/usr/bin/python3

"""
A script that displays all values in the states table of the database hbtn_0e_0_usa
whose name matches the one supplied as an argument.
Usage: ./filter_states_by_name.py <mysql username> <mysql password> <database name> <state name>
"""

import sys
import MySQLdb

def filter_states_by_name(username, password, database_name, state_name):
    try:
        db = MySQLdb.connect(user=username, passwd=password, db=database_name, host='localhost', port=3306)
        cursor = db.cursor()
        cursor.execute("SELECT * FROM states WHERE BINARY name = %s", (state_name,))
        data = cursor.fetchall()
        for row in data:
            print(row)
        cursor.close()
        db.close()
    except MySQLdb.Error as e:
        print("Error connecting to the database:", str(e))

if __name__ == '__main__':
    if len(sys.argv) != 5:
        print("Usage: ./filter_states_by_name.py <mysql username> <mysql password> <database name> <state name>")
        sys.exit(1)
    
    username, password, database_name, state_name = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]
    filter_states_by_name(username, password, database_name, state_name)
