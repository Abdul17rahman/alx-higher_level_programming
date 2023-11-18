#!/usr/bin/python3

""" Module to query the database for all states"""

from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model_state import Base, State


def list_states_with_a():
    """ Function that lists all states containing a"""
    session = Session()
    states = session.query(State).filter(State.name.like('%a%')).all()
    for state in states:
        print(f"{state.id}: {state.name}")
    session.close()


if __name__ == "__main__":
    import sys
    usr = sys.argv[1]
    pwd = sys.argv[2]
    db = sys.argv[3]
    host = "localhost"
    path = f'mysql+mysqldb://{usr}:{pwd}@{host}/{db}'
    engine = create_engine(path, pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    list_states_with_a()
