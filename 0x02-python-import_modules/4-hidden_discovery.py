#!/usr/bin/python3
if __name__ == '__main__':
    import hidden_4

    names = dir(hidden_4)
    names.sort()
    for name in names:
        if not(name[:2] is "__"):
            print(f"{name}")
