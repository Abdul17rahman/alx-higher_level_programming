#!/usr/bin/python3

"""
Module for the class definition of a State.
"""

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class State(Base):
    """
    State model that inherits from Base
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, autoincrement=True
                unique=True)
    name = Column(String(128), nullable=False)
