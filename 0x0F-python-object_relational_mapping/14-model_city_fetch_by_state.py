#!/usr/bin/python3
"""
This script prints all City objects
from the database `hbtn_0e_14_usa`.
"""

from sys import argv
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """
    Connect to the database and retrieve cities
    along with their associated states.
    """

    cust_db_connect_str = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1], argv[2], argv[3])
    engine = create_engine(cust_db_connect_str)
    CustomSession = sessionmaker(bind=engine)

    custom_session = CustomSession()

    custom_query = custom_session.query(City, State).join(State)

    for _city, _state in custom_query.all():
        print("{}: ({:d}) {}".format(_state.name, _city.id, _city.name))

    custom_session.commit()
    custom_session.close()
