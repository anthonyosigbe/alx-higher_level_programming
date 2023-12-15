#!/usr/bin/python3
"""
This script defines a State class and
a Base class for use with MySQLAlchemy ORM.
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """
    State class definition.

    Attributes:
        __tablename__ (str): The name of the corresponding table
        in the database.
        id (int): The unique identifier for each state.
        name (str): The name of the state.
        cities (:obj:`City`): Relationship attribute representing the
        cities associated with the state.
    """
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="all, delete")
