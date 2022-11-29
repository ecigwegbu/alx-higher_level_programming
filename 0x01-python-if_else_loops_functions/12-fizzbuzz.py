#!/usr/bin/python3
def fizzbuzz():
    for i in range(1, 101):
        out = ""
        if (i % 3) == 0:
            out = "Fizz"
        if (i % 5) == 0:
            out = out + "Buzz"
        if (out == ""):
            out = str(i)
        print(f"{out} ", end="")
