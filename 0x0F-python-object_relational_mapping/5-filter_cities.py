#!/usr/bin/python3
"""
This script takes in the name of a state
as an argument and lists all cities of that state
using the database hbtn_0e_4_usa.
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    """
    Connect to the database and retrieve
    all cities of the specified state.
    """

    if len(argv) != 5:
        print("Usage: {} <username> <password> <database>\
                <state_name>".format(argv[0]))
        exit(1)

    db_connection = MySQLdb.connect(host="localhost", user=argv[1], port=3306,
                                    passwd=argv[2], db=argv[3])

    cursor = db_connection.cursor()

    query = "SELECT cities.id, cities.name, states.name FROM cities \
             JOIN states ON cities.state_id = states.id \
             WHERE states.name LIKE BINARY %s \
             ORDER BY cities.id ASC"

    cursor.execute(query, (argv[4],))

    result_rows = cursor.fetchall()
    for result_row in result_rows:
        print(result_row)

    cursor.close()
    db_connection.close()
