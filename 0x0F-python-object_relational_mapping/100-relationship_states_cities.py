#!/usr/bin/python3
"""Script to create the state California with City San Francisco
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City


if __name__ == "__main__":
    c_str = 'mysql+mysqldb://{}:{}@localhost:3306/{}'
    engine = create_engine(c_str.format(sys.argv[1], sys.argv[2], sys.argv[3]))

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    california = State(name="California")
    san_francisco = City(name="San Francisco")
    california.cities.append(san_francisco)

    session.add(california)
    session.commit()
    session.close()
