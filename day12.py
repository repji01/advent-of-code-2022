#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""day02.py: Advent of Code 2022 --- Day 2: Paper Scissors ---
   https://adventofcode.com/2022/day/2
"""

__version__ = "1.0"
__maintainer__ = "Jiří Řepík"
__email__ = "jiri.repik@gmail.com"
__status__ = "Submited"

import argparse
import functools
import heapq
import math
import os
from typing import NamedTuple, Callable, Generator

import advent
from utils import *

TEST_DATA = """Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi"""
def download_input_data():
    advent.setup(2022, 12, dry_run=False)
    fin = advent.get_input()
    lines = fin.read()
    coords = {}
    for y, line in enumerate(TEST_DATA):
        for x, c in enumerate(line):
            coords[(y, x)] = c
            if c == 'S':
                #coords[(y, x)] = 'a'
                start = (y,x)
            if c == 'E':
                #coords[(y, x)] = 'z'
                end = (y,x)
    return (start, end, coords)



def adjacent_4(x: int, y: int) -> Generator[tuple[int, int], None, None]:
    yield x, y - 1
    yield x + 1, y
    yield x, y + 1
    yield x - 1, y

MAPPED = {
    'S' : chr(ord('a') - 1),
    'E' : chr(ord('z') + 1),
}
def part01(start, end, coords):
    seen = set()
    todo = [(0, start)]

    while todo:

        cost, pos = heapq.heappop(todo)
        print(f'pop {pos}')
        if pos == end:
            return cost
        elif pos in seen:
           continue
        else:
            seen.add(pos)

        for cand in adjacent_4(*pos):
            if cand in coords:
                current_c = MAPPED.get(coords[pos], coords[pos])
                cand_c = MAPPED.get(coords[cand], coords[cand])
                if ord(cand_c) - ord(current_c) <= 1:
                    print(f'push {cand}')
                    heapq.heappush(todo, (cost +1, cand))

    pass
    #advent.submit_answer(1, seen[-1] * seen[-2])

def part02(start, end, coords):
    pass
    #advent.submit_answer(2, seen[-1] * seen[-2])



if __name__ == "__main__":
    start, end, coords = download_input_data()
    timer_start()
    print(part01(start, end, coords))
    part02(start, end, coords)

