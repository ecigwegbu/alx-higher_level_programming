#!/usr/bin/python3
if __name__ == '__main__':
    from sys import argv
    from calculator_1 import add, sub, mul, div

    argc = len(argv)
    if argc != 4:
        print(f"Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    elif not ("+-*/".__contains__(argv[2])):
        print(f"Unknown operator. Available operators: +, -, * and /")
        exit(1)

    a = int(argv[1])
    b = int(argv[3])
    op = argv[2]
    if op == "+":
        c = a + b
        print("{:d} + {:d} = {:d}".format(a, b, c))
    elif op == "-":
        c = a - b
        print("{:d} - {:d} = {:d}".format(a, b, c))
    elif op == "/":
        c = a / b
        print("{:d} / {:d} = {}".format(a, b, c))
    elif op == "*":
        c = a * b
        print("{:d} * {:d} = {:d}".format(a, b, c))
