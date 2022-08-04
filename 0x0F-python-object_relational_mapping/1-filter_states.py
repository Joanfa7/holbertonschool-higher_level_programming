#!/usr/bin/python3
""" script that lists all states form the data base hbtn_0e_0_usa"""

import MySQLdb

if __name__ == "__main__":

    db = MySQLdb.connect(host="localhost", user="root", password="root",
                         database="hbtn_0e_0_usa")

    cursor = db.cursor()

    cursor.execute("Select * FROM states WHERE name LIKE 'N%' ORDER BY states.id ASC")

    result = cursor.fetchall()

    for row in result:
        print(row)
