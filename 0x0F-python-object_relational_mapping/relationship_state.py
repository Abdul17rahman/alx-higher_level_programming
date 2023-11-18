#!/usr/bin/python3

"""
Module for the class definition of a State.
"""

from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Column, Integer, String

Base = declarative_base()


class State(Base):
    """ State database class"""
    __tablename__ = "states"
    id = Column(Integer, nullable=False, primary_key=True, autoincrement=True)
    name = Column(String(128), nullable=False)
    cities = relationship('City', back_populates='state',
                          cascade='all, delete-orphan')
