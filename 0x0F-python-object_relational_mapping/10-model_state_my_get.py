#!/usr/bin/python3

"""
A script that lists the State object with the name passed as an argument
from the database hbtn_0e_6_usa.
Usage: ./model_state_my_get.py <mysql username> <mysql password> <database name> <state name searched>
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State

def get_state_by_name(username, password, database_name, state_name):
    try:
        engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                               .format(username, password, database_name),
                               pool_pre_ping=True)
        Session = sessionmaker(bind=engine)
        session = Session()

        state = session.query(State).filter(State.name == state_name).one_or_none()
        if state is not None:
            print("{}".format(state.id))
        else:
            print("Not found")

        session.close()
    except Exception as e:
        print("Error:", str(e))

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: ./model_state_my_get.py <mysql username> <mysql password> <database name> <state name searched>")
        sys.exit(1)
    
    username, password, database_name, state_name = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]
    get_state_by_name(username, password, database_name, state_name)
