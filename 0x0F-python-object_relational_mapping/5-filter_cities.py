#!/usr/bin/python3
""" script that lists all states form the data base hbtn_0e_0_usa"""

from sys import argv
import MySQLdb

if __name__ == "__main__":

    find_name = argv[4]

    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], database=argv[3])

    cursor = db.cursor()

    cursor.execute('SELECT cities.name FROM cities, states\
                   WHERE states.name = %(state_name)s AND states.id=state_id\
                   ORDER BY cities.id ASC', {'state_name': find_name})

    result = cursor.fetchall()
    city = ()
    for row in result:
        city += row
    print(', '.join(city))
    cursor.close()
    db.close()
