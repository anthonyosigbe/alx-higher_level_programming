#!/usr/bin/python3
"""
This script takes an argument and
displays all values in the states
where `name` matches the argument
from the database `hbtn_0e_0_usa`.
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    """
    Connect to the database and retrieve the states
    matching the specified argument.
    """

    db_connection = MySQLdb.connect(host="localhost", user=argv[1], port=3306,
                                    passwd=argv[2], db=argv[3])

    cursor = db_connection.cursor()
    cursor.execute("SELECT * FROM states \
                    WHERE name LIKE BINARY '{}' \
                    ORDER BY states.id ASC".format(argv[4]))
    result_rows = cursor.fetchall()

    for result_row in result_rows:
        print(result_row)
