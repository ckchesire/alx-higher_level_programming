#!/usr/bin/python3
"""Script that lists all State objects, and corresponding City objects
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from relationship_city import City
from relationship_state import Base, State


if __name__ == "__main__":
    c_str = 'mysql+mysqldb://{}:{}@localhost:3306/{}'
    engine = create_engine(c_str.format(sys.argv[1], sys.argv[2], sys.argv[3]))

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    run_query = session.query(State).order_by(State.id).all()

    for state in run_query:
        print("{}: {}".format(state.id, state.name))
        for city in state.cities:
            print("\t{}: {}".format(city.id, city.name))

    session.close()
