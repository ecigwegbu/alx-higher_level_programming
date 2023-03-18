#!/usr/bin/python3
'''Load a database'''

import MySQLdb
from sys import argv

if __name__ == "__main__":
    # print("Args :", argv[0], argv[1], argv[2])
    if (len(argv) != 4):
        exit()

    mydb = MySQLdb.connect(host='localhost', user=argv[1],
                           passwd=argv[2], db=argv[3], port=3306)
    cur = mydb.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")

    # Print results
    rows = cur.fetchall()
    for row in rows:
        if(row[1][0] == 'N'):
            print(row)
