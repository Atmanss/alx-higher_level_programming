#!/usr/bin/python3
"""Defines a City model.
Inherits from SQLAlchemy Base and links to the MySQL table cities.
"""

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base

The_Base = declarative_base()


class City(The_Base):
    """Represents a city on a MySQL database.

    Attributes:
        id 'sqlalchemy.Column': The city's id.
        name 'sqlalchemy.Column': The city's name.
        state_id 'sqlalchemy.Column: The city's state id.
    """
    __tablename__ = "cities"
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
