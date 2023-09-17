#!/usr/bin/python3

"""
A script that returns the first State object from hbtn_0e_6_usa.
Username, password, and dbname will be passed as arguments to the script.
"""

import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

def get_first_state(username, password, database_name):
    try:
        engine = create_engine(f'mysql+mysqldb://{username}:{password}@localhost:3306/{database_name}', pool_pre_ping=True)
        Session = sessionmaker(bind=engine)
        Base.metadata.create_all(engine)

        # Create a session
        session = Session()

        # Extract the first state
        state = session.query(State).order_by(State.id).first()

        # Print state
        if state is None:
            print("Nothing")
        else:
            print(f"{state.id}: {state.name}")
    except Exception as e:
        print("An error occurred:", str(e))
    finally:
        session.close()

if __name__ == '__main__':
    if len(sys.argv) != 4:
        print("Usage: ./script.py <mysql username> <mysql password> <database name>")
        sys.exit(1)

    username, password, database_name = sys.argv[1], sys.argv[2], sys.argv[3]
    get_first_state(username, password, database_name)
