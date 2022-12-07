#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""day05.py: Advent of Code 2022 --- Day 3: Rucksack Reorganization ---
   https://adventofcode.com/2022/day/3
"""

__version__ = "1.0"
__maintainer__ = "Jiří Řepík"
__email__ = "jiri.repik@gmail.com"
__status__ = "Submited"

import argparse
import collections
import os

import advent
from utils import *


def download_input_data():
    global fin
    advent.setup(2022, 6, dry_run=False)
    fin = advent.get_input()
    lines = fin.read()
    return lines


def part01(lines):
    d: collections.deque[str] = collections.deque(maxlen=4)

    for i, c in enumerate(lines.strip()):
        d.append(c)

        if len(d) == d.maxlen and len(set(d)) == d.maxlen:
            advent.submit_answer(1, i + 1)
            return


    raise NotImplementedError('wat')


def part02(lines):
    d: collections.deque[str] = collections.deque(maxlen=14)

    for i, c in enumerate(lines.strip()):
        d.append(c)

        if len(d) == d.maxlen and len(set(d)) == d.maxlen:
            advent.submit_answer(2, i + 1)
            return

    raise NotImplementedError('wat')


if __name__ == "__main__":
    lines = download_input_data()
    timer_start()

    print(part01(lines))
    print(part02(lines))
