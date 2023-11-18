#!/usr/bin/python3

"""
Module for the class definition of a State.
"""

from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, ForeignKey
from relationship_state import Base


class City(Base):
    """ State database class"""
    __tablename__ = "cities"
    id = Column(Integer, nullable=False, primary_key=True, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
    state = relationship('State', back_populates='cities')
