#!/usr/bin/python3
"""Module that lists all states with N from the database
"""

import MySQLdb
import sys


def get_states_by_name():
    """
        Method to that retrieves command-line arguments
        and runs query on mysql server instance
    """
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state = sys.argv[4]

    db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=database
        )

    c = db.cursor()
    query = "SELECT*FROM states WHERE name ='{}' ORDER BY id ASC".format(state)
    c.execute(query)
    rows = c.fetchall()

    for row in rows:
        print(row)

    c.close()
    db.close()


if __name__ == "__main__":
    get_states_by_name()
