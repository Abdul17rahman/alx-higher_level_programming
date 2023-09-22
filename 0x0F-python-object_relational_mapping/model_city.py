#!/usr/bin/python3

"""
Module for the class definition of a Cities.
"""

from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class City(Base):
    """
    Cities model that inherits from Base
    """
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, autoincrement=True
                nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
