#!/usr/bin/python3
'''Load and filter a database'''

import MySQLdb
from sys import argv
import re

if __name__ == "__main__":
    if (len(argv) != 5):
        exit()

    mydb = MySQLdb.connect(host='localhost', user=argv[1],
                           passwd=argv[2], db=argv[3], port=3306)
    cur = mydb.cursor()

    if (re.search('^[\\w ]*$', argv[4])):  # filter out possible SQL injection
        cur.execute("SELECT cities.id, cities.name, states.name "
                    "FROM cities JOIN states ON cities.state_id=states.id "
                    "WHERE states.name = '%s' "
                    "ORDER BY cities.id ASC" % argv[4])

        # Print results
        rows = cur.fetchall()
        if (rows):
            print(rows[0][1], end="")
            # for i in range(1, 3):
            for i in range(1, len(rows)):
                print(',', rows[i][1], end="")
            print("")

        # clean up
        cur.close()
        mydb.close()
