#!/usr/bin/python3
""" script that lists all states form the data base hbtn_0e_0_usa"""

from sys import argv
import MySQLdb

if __name__ == "__main__":

    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], database=argv[3])

    cursor = db.cursor()

    cursor.execute("Select * FROM states WHERE name LIKE 'N%' ORDER\
                    BY states.id ASC")

    result = cursor.fetchall()

    for row in result:
        if row[1][0] == 'N':
            print(row)
    cursor.close()
    db.close()
