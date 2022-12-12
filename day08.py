#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""day08.py: Advent of Code 2022 --- Day 7: Rucksack Reorganization ---
   https://adventofcode.com/2022/day/7
"""

__version__ = "1.0"
__maintainer__ = "Jiří Řepík"
__email__ = "jiri.repik@gmail.com"
__status__ = "Submited"

import argparse
import collections
import os

import advent
import argparse
from utils import *
from utils.helpers import parse_coords_int


def download_input_data():
    global fin
    advent.setup(2022, 8, dry_run=False)
    fin = advent.get_input()
    cords = parse_coords_int(fin.read())
    return cords

SAMPLE = """$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k"""



def part01(coords):
    visible = set()

    ymin, xmin = min(coords)
    ymax, xmax = max(coords)

    for y in range(ymin, ymax + 1):
        # down
        val = coords[(y, xmin)]
        visible.add((y, xmin))
        for x in range(xmin + 1, xmax + 1):
            cand = (y, x)
            if coords[cand] > val:
                visible.add(cand)
                val = coords[cand]

        # up
        val = coords[(y, xmax)]
        visible.add((y, xmax))
        for x in range(xmax, -1, -1):
            cand = (y, x)
            if coords[cand] > val:
                visible.add(cand)
                val = coords[cand]

    for x in range(xmin, xmax + 1):
        # right
        val = coords[(ymin, x)]
        visible.add((ymin, x))
        for y in range(ymin + 1, ymax + 1):
            cand = (y, x)
            if coords[cand] > val:
                visible.add(cand)
                val = coords[cand]

        # left
        val = coords[(ymax, x)]
        visible.add((ymax, x))
        for y in range(ymax, -1, -1):
            cand = (y, x)
            if coords[cand] > val:
                visible.add(cand)
                val = coords[cand]

    return len(visible)


    # advent.submit_answer(1, i + 1)



def part02(lines):
   pass


if __name__ == "__main__":
    coords = download_input_data()
    timer_start()

    print(part01(coords))
    print(part02(coords))
