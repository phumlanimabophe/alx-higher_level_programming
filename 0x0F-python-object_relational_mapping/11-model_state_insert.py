#!/usr/bin/python3

"""
A script that adds the State object 'Louisiana' to the database hbtn_0e_6_usa.
Usage: ./model_state_insert.py <mysql username> <mysql password> <database name>
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

def insert_state(username, password, database_name):
    try:
        engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                               .format(username, password, database_name),
                               pool_pre_ping=True)
        Session = sessionmaker(bind=engine)

        Base.metadata.create_all(engine)

        # create a session
        session = Session()

        # create the object and add it
        new_state = State(name='Louisiana')
        session.add(new_state)
        session.commit()

        # print state.id
        state_add = session.query(State).filter(State.name == 'Louisiana').one()
        print(state_add.id)

        session.close()
    except Exception as e:
        print("Error:", str(e))

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: ./model_state_insert.py <mysql username> <mysql password> <database name>")
        sys.exit(1)
    
    username, password, database_name = sys.argv[1], sys.argv[2], sys.argv[3]
    insert_state(username, password, database_name)
