#!/usr/bin/python

import sys


def climbing_stairs(n, cache=None):
    if n < 0:
        return 0
    if n == 0:  # return 1 instead of 0 because there is one way to climb zero stairs
        return 1
    if n >= 1:
        return climbing_stairs(n - 3) + climbing_stairs(n - 2) + climbing_stairs(n - 1)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_stairs = int(sys.argv[1])
        print("There are {ways} ways for a child to jump {n} stairs.".format(
            ways=climbing_stairs(num_stairs), n=num_stairs))
    else:
        print('Usage: climbing_stairs.py [num_stairs]')

print(climbing_stairs(10))
