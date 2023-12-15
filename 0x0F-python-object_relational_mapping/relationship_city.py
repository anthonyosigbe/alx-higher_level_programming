#!/usr/bin/python3
"""
This script defines a City class
for use with MySQLAlchemy ORM.
"""

from relationship_state import Base, State
from sqlalchemy import Column, Integer, String, ForeignKey


class City(Base):
    """
    City class definition.

    Attr:
        __tablename__ (str): The name of the corresponding table
        in the database.
        id (int): The unique identifier for each city.
        name (str): The name of the city.
        state_id (int): The foreign key linking the city
        to its corresponding state.
    """
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
