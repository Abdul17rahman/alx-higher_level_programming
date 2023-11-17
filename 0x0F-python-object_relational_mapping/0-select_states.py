#!/usr/bin/python3

import MySQLdb
import sys


username = sys.argv[1]
password = sys.argv[2]
db_name = sys.argv[3]

print(username, password, db_name)
conn = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=db_name, charset="utf8")

cur = conn.cursor()

cur.execute("Select * from states order by states.id asc")

query_rows = cur.fetchall()
for row in query_rows:
    print(row)
cur.close()
conn.close()
