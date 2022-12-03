#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""day01.py: Advent of Code 2022 --- Day 3: Rucksack Reorganization ---
   https://adventofcode.com/2022/day/3
"""

__version__ = "1.0"
__maintainer__ = "Jiří Řepík"
__email__ = "jiri.repik@gmail.com"
__status__ = "Submited"

import argparse
import os

import advent
from utils import *


def download_input_data():
    global fin
    advent.setup(2022, 3, dry_run=False)
    fin = advent.get_input()
    lines = get_lines(fin.readlines())
    return lines


def part01(lines):
    value = 0

    for line in lines:
        items = [line[:len(line) // 2], line[len(line) // 2:]]
        item, = set(items[0]) & set(items[1])
        if item.isupper():
            value += 27 + ord(item) - ord('A')
        else:
            value += 1 + ord(item) - ord('a')

    advent.submit_answer(1, value)

def part02(lines):
    value = 0
    items = iter(lines)

    while True:
        try:
            item, = set(next(items)) & set(next(items)) & set(next(items))
        except StopIteration:
            break
        else:
            if item.isupper():
                value += 27 + ord(item) - ord('A')
            else:
                value += 1 + ord(item) - ord('a')

    advent.submit_answer(2, value)


if __name__ == "__main__":
    lines = download_input_data()
    timer_start()

    part01(lines)
    part02(lines)
