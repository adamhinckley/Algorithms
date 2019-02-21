#!/usr/bin/python

import sys
import itertools

rps = ["rock", "paper", "scissors"]


def rock_paper_scissors(n):
  # itertools.product iterates over the list and returns every possible combination it's told to repeat
  # https://docs.python.org/2/library/itertools.html search for itertools.product
    result = list(itertools.product(rps, repeat=n))

    return [list(e) for e in result]


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_plays = int(sys.argv[1])
        print(rock_paper_scissors(num_plays))
    else:
        print('Usage: rps.py [num_plays]')

print(rock_paper_scissors(3))
