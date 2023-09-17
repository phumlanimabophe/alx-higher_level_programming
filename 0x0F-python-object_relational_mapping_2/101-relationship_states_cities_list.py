#!/usr/bin/python3

"""
Lists all States and corresponding Cities in the database hbtn_0e_101_usa.
Usage: ./101-relationship_states_cities_list.py <mysql username> <mysql password> <database name>
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import State

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: ./101-relationship_states_cities_list.py <mysql username> <mysql password> <database name>")
        sys.exit(1)

    username, password, database_name = sys.argv[1], sys.argv[2], sys.argv[3]
    
    # Create the database connection
    engine = create_engine(f"mysql+mysqldb://{username}:{password}@localhost/{database_name}", pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query and print States and their Cities
    for state in session.query(State).order_by(State.id):
        print(f"{state.id}: {state.name}")
        for city in state.cities:
            print(f"    {city.id}: {city.name}")
