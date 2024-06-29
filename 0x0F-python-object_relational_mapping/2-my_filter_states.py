#!/usr/biin/python3
    """ a script that takes in an argument and displays all values in the states t          able of hbtn_0e_0_usa where name matches the argument.
    """

import MySQLdb
import sys

def main():
    """ list all values that matches the user input
    """     

    host = 'localhost'
    port = 3306
    user = sys.argv[1]
    passwd = sys.argv[2]
    db = sys.argv[3]
    UserInput = sys.argv[4]

    db = MySQLdb.connect(
            HOST = host,
            PORT = port,
            USER = user,
            PASSWD = passwd,
            DB = db
    )

    cur = db.cursor()
    firstQuery = "SELECT id, name FROM states WHERE name"
    secondQuery = "LIKE BINARY '{}' ORDER id by ASC".format(UserInput)
    finalQuery = firstQuery + secondQuery
    cur.execute(finalQuery)
    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    db.close()

if __name__ == "__main__":
    main()
