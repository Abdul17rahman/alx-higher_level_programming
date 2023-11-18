#!/usr/bin/python3


from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String


Base = declarative_base()

class State(Base):
    """ State database class"""
    __tablename__ = "states"
    id = Column(Integer, unique=True, primary_key=True, autoincrement=True)
    name = Column(String(128), nullable=False)
