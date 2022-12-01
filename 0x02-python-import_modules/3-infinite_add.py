#!/usr/bin/python3
if __name__ == '__main__':
    from sys import argv

    na = len(argv)  # na == nr of args, excluding the command
    total = 0
    for arg in range(1, na):
        total += int(argv[arg])
    print(f"{total:d}")
