#!/usr/bin/python3

"""
Module for the class definition of a State.
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """
    State model that inherits from Base
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, autoincrement=True
                nullable=False)
    name = Column(String(128), nullable=False)
