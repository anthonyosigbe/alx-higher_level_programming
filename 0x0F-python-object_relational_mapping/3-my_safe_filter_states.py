#!/usr/bin/python3
"""
This script takes in arguments and displays
all values in the states table of hbtn_0e_0_usa
where name matches the argument, preventing
SQL injection.
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    """
    Connect to the database and retrieve the states
    matching the specified argument using parameterized query.
    """

    if len(argv) != 5:
        print("Usage: {} <username> <password> <database>\
                <state_name>".format(argv[0]))
        exit(1)

    db_connection = MySQLdb.connect(host="localhost", user=argv[1], port=3306,
                                    passwd=argv[2], db=argv[3])

    cursor = db_connection.cursor()

    query = "SELECT * FROM states WHERE\
            name LIKE BINARY %s\
            ORDER BY states.id ASC"
    cursor.execute(query, (argv[4],))

    result_rows = cursor.fetchall()
    for result_row in result_rows:
        print(result_row)

    cursor.close()
    db_connection.close()
