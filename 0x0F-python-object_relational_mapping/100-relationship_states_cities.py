#!/usr/bin/python3
"""
This script prints all City objects
from the database `hbtn_0e_14_usa`.
"""

from sys import argv
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """
    Connect to the database and add a new state
    with an associated city, then commit the changes.
    """

    cust_db_connect_str = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1], argv[2], argv[3])
    engine = create_engine(cust_db_connect_str)
    Base.metadata.create_all(engine)
    CustomSession = sessionmaker(bind=engine)

    custom_session = CustomSession()

    custom_state = State(name='California')
    custom_city = City(name='San Francisco')
    custom_state.cities.append(custom_city)

    custom_session.add(custom_state)
    custom_session.commit()
    custom_session.close()
