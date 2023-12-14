#!/usr/bin/python3
"""
This script retrieves and displays all states with
a `name` starting with the letter `N` from the
MySQL database named `hbtn_0e_0_usa`.
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    """
    Establish a connection to the MySQL database and fetch the states
    with names starting with 'N'. Display the results in ascending order
    based on the state ID.
    """
    db_connection = MySQLdb.connect(host="localhost", user=argv[1], port=3306,
                                    passwd=argv[2], db=argv[3])

    db_cursor = db_connection.cursor()

    db_cursor.execute("SELECT * FROM states \
                       WHERE name LIKE BINARY 'N%' \
                       ORDER BY states.id ASC")

    selected_states = db_cursor.fetchall()

    for state_data in selected_states:
        print(state_data)
