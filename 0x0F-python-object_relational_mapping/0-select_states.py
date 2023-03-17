#!/usr/bin/python3
'''Load a database'''

import MySQLdb

if __name__ == "__main__":

    mydb = MySQLdb.connect(host='localhost', user='root',
                           passwd='password', db='hbtn_0e_0_usa', port=3306)
    cur = mydb.cursor()
    numrows = cur.execute("SELECT * FROM states")
    print("Selected " + str(numrows) + " rows")
