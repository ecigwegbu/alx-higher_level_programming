#!/usr/bin/python3
if __name__ == '__main__':
    from sys import argv

    argc = len(argv)
    if argc != 4:
        print(f"Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    elif not (r"+-*/".__contains__(argv[2])):
        print(f"Unknown operator. Available operators: +, -, * and /")
        exit(1)

    from calculator_1 import add, sub, mul, div
    a = int(argv[1])
    b = int(argv[3])
    op = argv[2]
    match op:
        case "+":
            print(f"{a} + {b} = {a + b}")
        case "-":
            print(f"{a} - {b} = {a - b}")
        case "*":
            print(f"{a} * {b} = {a * b}")
        case "/":
            print(f"{a} / {b} = {a / b}")
