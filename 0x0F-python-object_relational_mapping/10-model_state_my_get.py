#!/usr/bin/python3

""" Module to query the database for all states"""

from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model_state import Base, State


def list_state_name(name):
    """ Function that lists all states containing a"""
    session = Session()
    state = session.query(State).filter(State.name == name).first()
    if state:
        print(f"{state.id}")
    else:
        print("Not found")
    session.close()


if __name__ == "__main__":
    import sys
    usr = sys.argv[1]
    pwd = sys.argv[2]
    db = sys.argv[3]
    name = sys.argv[4]
    host = "localhost"
    path = f'mysql+mysqldb://{usr}:{pwd}@{host}/{db}'
    engine = create_engine(path, pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    list_state_name(name)
