#!/usr/bin/python3
'''Load and filter a database'''

import MySQLdb
from sys import argv
import re

if __name__ == "__main__":
    if (len(argv) != 4):
        exit()

    mydb = MySQLdb.connect(host='localhost', user=argv[1],
                           passwd=argv[2], db=argv[3], port=3306)
    cur = mydb.cursor()
    if (re.search('^[\\w ]*$', argv[4])):  # regex matches words and spcs only
        cur.execute("SELECT * FROM cities ORDER BY id ASC"
                    % argv[3])

        # Print results
        rows = cur.fetchall()
        for row in rows:
            print(row)

        # clean up
        cur.close()
        mydb.close()
