#!/usr/bin/python3
"""
Contains state class Base instance for SQLAlchemy
"""
from sqlalchemy import Column, Integer, String, MetaData
from sqlalchemy.ext.declarative import declarative_base

my_metadata = MetaData()

Base = declarative_base(metadata=my_metadata)


class State(Base):
    """State class tha inherits from Base

       Attributes/Fields:
          id(int): Primary key for the state
          name(str): Name of the state
    """
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
