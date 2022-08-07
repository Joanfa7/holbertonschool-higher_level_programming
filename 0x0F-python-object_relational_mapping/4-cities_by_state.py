#!/usr/bin/python3
""" script that lists all states form the data base hbtn_0e_0_usa"""

from sys import argv
import MySQLdb

if __name__ == "__main__":

    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], database=argv[3])

    cursor = db.cursor()

    cursor.execute('SELECT cities.id, cities.name, states.name\
                   FROM cities, states WHERE states.id=state_id')

    result = cursor.fetchall()

    for row in result:
        print(row)
    cursor.close()
    db.close()
