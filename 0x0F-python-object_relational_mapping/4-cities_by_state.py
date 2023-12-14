#!/usr/bin/python3
"""
This script lists all cities from the database hbtn_0e_4_usa.
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    """
    Connect to the database and retrieve all cities.
    """

    if len(argv) != 4:
        print("Usage: {} <username> <password> <database>".format(argv[0]))
        exit(1)

    db_connection = MySQLdb.connect(host="localhost", user=argv[1], port=3306,
                                    passwd=argv[2], db=argv[3])

    cursor = db_connection.cursor()

    cursor.execute("SELECT cities.id, cities.name, states.name FROM cities \
                    JOIN states ON cities.state_id = states.id \
                    ORDER BY cities.id ASC")

    result_rows = cursor.fetchall()
    for result_row in result_rows:
        print(result_row)

    cursor.close()
    db_connection.close()
