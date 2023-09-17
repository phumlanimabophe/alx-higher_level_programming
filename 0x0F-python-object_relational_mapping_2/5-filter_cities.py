#!/usr/bin/python3

"""
A script that lists all cities in a state from the database hbtn_0e_0_usa.
Username, password, database name, and state are given as user args.
"""

import sys
import MySQLdb

def list_cities_by_state(username, password, database_name, state_name):
    try:
        db = MySQLdb.connect(user=username,
                             passwd=password,
                             db=database_name,
                             host='localhost',
                             port=3306)
        cursor = db.cursor()

        sql = """SELECT cities.name
                 FROM states
                 INNER JOIN cities ON states.id = cities.state_id
                 WHERE states.name = %s
                 ORDER BY cities.id ASC"""

        cursor.execute(sql, (state_name,))
        data = cursor.fetchall()

        print(", ".join([city[0] for city in data]))
    except MySQLdb.Error as e:
        print(f"An error occurred: {e}")
    finally:
        cursor.close()
        db.close()

if __name__ == '__main__':
    if len(sys.argv) != 5:
        print("Usage: ./script.py <mysql username> <mysql password> <database name> <state name>")
        sys.exit(1)

    username, password, database_name, state_name = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]
    list_cities_by_state(username, password, database_name, state_name)
