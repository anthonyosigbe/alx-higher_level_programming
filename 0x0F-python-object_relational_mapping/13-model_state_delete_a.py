#!/usr/bin/python3
"""
This script deletes all State objects
with a name containing the letter `a`
from the database `hbtn_0e_6_usa`.
"""

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """
    Delete State objects in the database
    with names containing the letter 'a'.
    """

    cust_db_connect_str = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1], argv[2], argv[3])
    engine = create_engine(cust_db_connect_str)
    CustomSession = sessionmaker(bind=engine)

    cust_sess = CustomSession()

    for instance in cust_sess.query(State).filter(State.name.contains('a')):
        cust_sess.delete(instance)

    cust_sess.commit()
