#!/usr/bin/python3
if __name__ == '__main__':
    from sys import argv
    na = len(argv) - 1  # na == nr of args, excluding the command
    s = "s"             # optional plural
    if na == 1:
        s = ""
    end = "."
    if na != 0:
        end = ":"
    print(f"{na:d} argument{s}{end}")
    for arg in range(1, na + 1):
        print(f"{arg}: {argv[arg]}")
