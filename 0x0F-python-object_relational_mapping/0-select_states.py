#!/usr/bin/python3

import MySQLdb
import sys


def list_states(username, password, database):
    """ Functions that finds states """
    db = MySQLdb.connect(  # Connect to the database
        user=username,
        passwd=password,
        db=database
    )

    # Create a cursor object to interact with the database
    cursor = db.cursor()

    # Execute the SQL query to select all states
    cursor.execute("SELECT * FROM states")

    # Fetch all the rows
    rows = cursor.fetchall()

    # Print the list of states
    for row in rows:
        print(row)

    # Close the cursor and database connection
    cursor.close()
    db.close()


if __name__ == "__main__":
    username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]
    list_states(username, password, database)
