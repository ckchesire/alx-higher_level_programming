#!/usr/bin/python3
"""Script that lists all State objects, and corresponding City objects
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_city import City
from relationship_state import Base, State


if __name__ == "__main__":
    c_str = 'mysql+mysqldb://{}:{}@localhost:3306/{}'
    engine = create_engine(c_str.format(sys.argv[1], sys.argv[2], sys.argv[3]))

    Session = sessionmaker(bind=engine)
    session = Session()

    run_query = session.query(City).order_by(City.id).all()

    for city in run_query:
        print("{}: {} -> {}".format(city.id, city.name, city.state.name))

    session.close()
