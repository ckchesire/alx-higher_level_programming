#!/usr/bin/python3
"""Script that prints all City objects from the database hbtn_0e_14_usa
"""

import sys
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    conn_str = 'mysql+mysqldb://{}:{}@localhost:3306/{}'
    engine = create_engine(conn_str.format(
        sys.argv[1],
        sys.argv[2],
        sys.argv[3]),
        pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()
    for instance in session.query(State.name, City.id, City.name)\
            .filter(State.id == City.state_id):
        print("{}: ({}) {}".format(instance[0], instance[1], instance[2]))
    session.commit()
    session.close()
