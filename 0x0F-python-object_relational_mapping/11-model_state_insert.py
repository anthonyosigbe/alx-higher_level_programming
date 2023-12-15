#!/usr/bin/python3
"""
This script adds the State object
`Louisiana` to the database `hbtn_0e_6_usa`.
"""

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """
    Connect to the database, add a new state,
    and print the new state's id.
    """

    cust_db_connect_str = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1], argv[2], argv[3])
    engine = create_engine(cust_db_connect_str)
    Session = sessionmaker(bind=engine)

    custom_session = Session()

    new_state_object = State(name='Louisiana')
    custom_session.add(new_state_object)
    custom_session.commit()
    print('{0}'.format(new_state_object.id))
    custom_session.close()
