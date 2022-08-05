#!/usr/bin/python3
""" script that lists all states form the data base hbtn_0e_0_usa"""

import sys
import MySQLdb

if __name__ == "__main__":

    find_name = sys.argv[4]

    db = MySQLdb.connect(host="localhost", port=3306, user="root", password="root",
                         database="hbtn_0e_0_usa")

    cursor = db.cursor()

    cursor.execute('Select * FROM states WHERE name LIKE "{}%" ORDER BY states.id ASC'
                   .format(find_name))

    result = cursor.fetchall()

    for row in result:
        print(row)
    curs.close()
    connector.close()

