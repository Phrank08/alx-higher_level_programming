#!/usr/bin/python3
""" lists all states from the database hbtn_0e_0_usa:
"""

import MySQLdb
import sys

def main():

    HOST = 'localhost'
    PORT = 3306
    USER = sys.argv[1]
    PASS = sys.argv[2]
    DB = sys.argv[3]

    database = MySQLdb.connect(
            host = HOST,
            port = PORT,
            user = USER,
            passwd = PASS,
            db = DB
    )
    cur = database.cursor()
    cur.execute("SELECT id, name FROM states ORDER BY id ASC")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    database.close()


if __name__ == "__main__":
    main()
