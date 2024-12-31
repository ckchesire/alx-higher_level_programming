#!/usr/bin/python3
"""Module that lists all rows from the database
"""

import MySQLdb
import sys


def get_all_states():
    """
        Method to that retrieves command-line arguments
        and runs query on mysql server instance
    """
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=database
        )

    c = db.cursor()
    c.execute("SELECT * FROM states ORDER BY id ASC")
    rows = c.fetchall()

    for row in rows:
        print(row)

    c.close()
    db.close()


if __name__ == "__main__":
    get_all_states()
