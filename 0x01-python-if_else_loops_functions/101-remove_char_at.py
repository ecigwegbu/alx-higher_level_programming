#!/usr/bin/python3
def remove_char_at(st, n):
    if n < 0 or n >= len(st):
        return st
    else:
        return f"{st[:n]}{st[n + 1:]}"
