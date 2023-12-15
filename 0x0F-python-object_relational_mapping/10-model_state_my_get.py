#!/usr/bin/python3
"""
This script prints the State object id
with the name passed as an argument
from the database `hbtn_0e_6_usa`.
"""

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """
    Connect to the database and retrieve a state
    based on the specified name.
    """

    db_connection_string = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1], argv[2], argv[3])
    engine = create_engine(db_connection_string)
    Session = sessionmaker(bind=engine)

    cust_ses = Session()
    state_ins = cust_ses.query(State).filter(State.name == argv[4]).first()

    if state_ins is None:
        print('Not found')
    else:
        print('{0}'.format(state_ins.id))
