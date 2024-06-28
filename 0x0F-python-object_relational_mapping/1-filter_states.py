#!/usr/bin/python3

""" lists all states with a name starting with N (upper N) from the database hbtn_0e_0_usa
"""
import MySQLdb
from sys import argv

def main():
    """
        lists all states beginning with letter 'N' in ascending order
    """
    My_Host = 'localhost'
    My_Port = 3306
    My_User = sys.argv[1]
    My_Passwd = sys.argv[2]
    My_db = sys.argv[3]

    db = MySQLdb.connect(
            HOST = My_Host,
            PORT = My_Port,
            USER = My_User,
            PASSWD = My_Passwd,
            db = My_db
    )

    MyCur = db.cursor()
    first_query = "SELECT id, name FROM states WHERE name"
    second_query = "LIKE BINARY 'N%' ORDER BY id ASC"
    final_query = first_query + second_query
    Mycur.execute(final_query)
    rows = Mycur.fetchall()
    for row in rows:
        print(row)
    MyCur.close()
    db.close()


if __name__ == "__main__":
    main()
