#!/usr/bin/python3
"""
  This is a script that lists all states from the database hbtn_0e_0_usa
    using MySQLdb ORM
"""


def select_states(username, password, database, state):
    """ Function that print the states """
    import MySQLdb

    database = MySQLdb.connect(user=username, passwd=password, db=database)
    cur = database.cursor()
    cur.execute("""SELECT cities.id, cities.name, states.name
                FROM cities
                INNER JOIN states ON cities.state_id = states.id
                WHERE states.name = %s
                ORDER BY cities.id ASC;""", (state,))
    items = cur.fetchall()
    print(', '.join(item[1] for item in items))
    cur.close()
    database.close()


if __name__ == "__main__":
    import sys
    usr = sys.argv[1]
    pwd = sys.argv[2]
    db = sys.argv[3]
    state = sys.argv[4]
    select_states(usr, pwd, db, state)
