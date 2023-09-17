#!/usr/bin/python3

"""
A script that deletes all State objects with a name containing the letter 'a'
from the database hbtn_0e_6_usa.
Usage: ./model_state_delete_a.py <mysql username> <mysql password> <database name>
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

def delete_states_with_a(username, password, database_name):
    try:
        engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                               .format(username, password, database_name),
                               pool_pre_ping=True)
        Session = sessionmaker(bind=engine)

        Base.metadata.create_all(engine)

        # create a session
        session = Session()

        # extract states with 'a' in their names
        states = session.query(State).filter(State.name.ilike('%a%')).all()

        # delete states
        for state in states:
            session.delete(state)

        session.commit()

        session.close()
    except Exception as e:
        print("Error:", str(e))

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: ./model_state_delete_a.py <mysql username> <mysql password> <database name>")
        sys.exit(1)
    
    username, password, database_name = sys.argv[1], sys.argv[2], sys.argv[3]
    delete_states_with_a(username, password, database_name)
