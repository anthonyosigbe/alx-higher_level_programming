#!/usr/bin/python3
"""
This script changes the name of a State object
from the database `hbtn_0e_6_usa`.
"""

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """
    Update the name of a State object in the database.
    """

    cust_db_connect_str = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1], argv[2], argv[3])
    engine = create_engine(cust_db_connect_str)
    Session = sessionmaker(bind=engine)

    custom_session = Session()

    target_state = custom_session.query(State).filter(State.id == '2').first()
    target_state.name = 'New Mexico'
    custom_session.commit()
    custom_session.close()
