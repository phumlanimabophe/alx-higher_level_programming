#!/usr/bin/python3

"""
A script that lists all cities of the database hbtn_0e_4_usa, ordered by city id.
Usage: ./cities_by_state.py <mysql username> <mysql password> <database name>
"""

import sys
import MySQLdb

def list_cities_by_state(username, password, database_name):
    try:
        db = MySQLdb.connect(user=username, passwd=password, db=database_name, host='localhost', port=3306)
        cursor = db.cursor()
        cursor.execute("SELECT c.id, c.name, s.name FROM cities c INNER JOIN states s ON c.state_id = s.id ORDER BY c.id")
        data = cursor.fetchall()
        for row in data:
            print(row)
        cursor.close()
        db.close()
    except MySQLdb.Error as e:
        print("Error connecting to the database:", str(e))

if __name__ == '__main__':
    if len(sys.argv) != 4:
        print("Usage: ./cities_by_state.py <mysql username> <mysql password> <database name>")
        sys.exit(1)
    
    username, password, database_name = sys.argv[1], sys.argv[2], sys.argv[3]
    list_cities_by_state(username, password, database_name)
