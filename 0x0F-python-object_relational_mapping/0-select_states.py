#!/usr/bin/python3

import MySQLdb


def select(usr, pwd, db):
    conn = MySQLdb.connect(user=usr, passwd=pwd, db=db, charset="utf8")

    cur = conn.cursor()

    cur.execute("Select * from states")

    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()


if __name__ == "__main__":
    import sys
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    select(username, password, db_name)
