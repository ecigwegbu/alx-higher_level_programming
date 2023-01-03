#!/usr/bin/python3
count = -1
def magic_string():
    global count
    count += 1
    list = "BestSchool"
    return list + ", BestSchool" * count 
