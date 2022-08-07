#!/usr/bin/python3
""" script that lists all states form the data base hbtn_0e_0_usa"""

from sys import argv
import MySQLdb

if __name__ == "__main__":

    find_name = argv[4]
    query = "Select * FROM states WHERE name = %s"

    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], database=argv[3])

    cursor = db.cursor()

    cursor.execute(query, (find_name,))

    result = cursor.fetchall()

    for row in result:
        print(row)
    cursor.close()
    db.close()
