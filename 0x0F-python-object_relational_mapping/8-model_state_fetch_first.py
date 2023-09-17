#!/usr/bin/python3

"""
A script that prints the first State object from the database hbtn_0e_6_usa.
Usage: ./model_state_fetch_first.py <mysql username> <mysql password> <database name>
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

def fetch_first_state(username, password, database_name):
    try:
        engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                               .format(username, password, database_name),
                               pool_pre_ping=True)
        Session = sessionmaker(bind=engine)
        session = Session()

        state = session.query(State).order_by(State.id).first()
        if state is None:
            print("Nothing")
        else:
            print("{}: {}".format(state.id, state.name))

        session.close()
    except Exception as e:
        print("Error:", str(e))

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: ./model_state_fetch_first.py <mysql username> <mysql password> <database name>")
        sys.exit(1)
    
    username, password, database_name = sys.argv[1], sys.argv[2], sys.argv[3]
    fetch_first_state(username, password, database_name)
