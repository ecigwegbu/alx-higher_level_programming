#!/usr/bin/python3
'''Load and filter a database'''

import MySQLdb
from sys import argv


def addSlashes(string):
    ''' add escape slashes to special characters in a string'''
    string = string.replace("\'", "\\\'")
    string = string.replace("*", "\\*")
    string = string.replace(";", "\\;")
    string = string.replace('\"', '\\\"')
    return string


if __name__ == "__main__":
    # print("Args :", argv[0], argv[1], argv[2])
    if (len(argv) != 5):
        exit()

    state = addSlashes(argv[4])
    print("Modified: ", state)
    print("QUERY: SELECT * FROM states WHERE name = '%s' ORDER BY id ASC"
          % state)
    mydb = MySQLdb.connect(host='localhost', user=argv[1],
                           passwd=argv[2], db=argv[3], port=3306)
    cur = mydb.cursor()
    cur.execute("SELECT * FROM states WHERE name = '%s' ORDER BY id ASC"
                % state)

    # Print results
    rows = cur.fetchall()
    for row in rows:
        print(row)
