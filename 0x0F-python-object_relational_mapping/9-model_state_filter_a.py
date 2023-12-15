#!/usr/bin/python3
"""
This script lists all State objects that contain the letter a
from the database `hbtn_0e_6_usa`.
"""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    """
    Access the database and print State objects
    containing the letter 'a'.
    """

    if len(argv) != 4:
        print("Usage: {} <username> <password> <database>".format(argv[0]))
        exit(1)

    db_connection_string = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1], argv[2], argv[3])

    engine = create_engine(db_connection_string)
    Session = sessionmaker(bind=engine)
    session = Session()

    states_with_a = session.query(State).filter
    (State.name.like('%a%')).order_by(State.id).all()

    if states_with_a:
        for state in states_with_a:
            print('{}: {}'.format(state.id, state.name))
    else:
        print("Nothing")
