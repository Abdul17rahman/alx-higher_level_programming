#!/usr/bin/python3

""" Module to query the database for all states"""

from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from relationship_state import Base, State
from relationship_city import City


def filter_state():
    """ Function that adds both state and city"""
    session = Session()
    cities = session.query(City).order_by(City.id)
    for city in cities:
        print(f"{city.id}: {city.name} -> {city.state.name}")
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
    filter_state()
