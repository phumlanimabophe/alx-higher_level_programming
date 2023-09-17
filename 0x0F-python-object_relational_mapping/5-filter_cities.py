#!/usr/bin/python3

"""
A script that displays all cities of a given state from the states table of the database hbtn_0e_4_usa.
Safe from SQL injections.
Usage: ./filter_cities_by_state.py <mysql username> <mysql password> <database name> <state name>
"""

import sys
import MySQLdb

def filter_cities_by_state(username, password, database_name, state_name):
    try:
        db = MySQLdb.connect(user=username, passwd=password, db=database_name, host='localhost', port=3306)
        cursor = db.cursor()
        cursor.execute("SELECT cities.name FROM cities INNER JOIN states ON cities.state_id = states.id WHERE states.name = %s ORDER BY cities.id", (state_name,))
        data = cursor.fetchall()
        city_names = [city[0] for city in data]
        print(", ".join(city_names))
        cursor.close()
        db.close()
    except MySQLdb.Error as e:
        print("Error connecting to the database:", str(e))

if __name__ == '__main__':
    if len(sys.argv) != 5:
        print("Usage: ./filter_cities_by_state.py <mysql username> <mysql password> <database name> <state name>")
        sys.exit(1)
    
    username, password, database_name, state_name = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]
    filter_cities_by_state(username, password, database_name, state_name)
