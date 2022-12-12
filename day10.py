#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""day01.py: Advent of Code 2022 --- Day 2: Calorie Counting ---
   https://adventofcode.com/2022/day/1
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
    global lines
    advent.setup(2022, 10, dry_run=False)
    fin = advent.get_input()
    lines = iter(fin.readlines())
    return lines

INTERESTING = {20, 60, 100, 140, 180, 220}

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'inputs/2022_10.txt')
def part01(s):
    interesting_sums = 0

    x = 1
    lines = iter(s.splitlines())
    instr_n = 0
    instr = 'noop'

    for i in range(1, 220 + 1):
        if instr_n == 0:
            instr = next(lines)
            if instr == 'noop':
                instr_n = 1
            elif instr.startswith('addx '):
                instr_n = 2

        instr_n -= 1

        if i in INTERESTING:
            interesting_sums += x * i

        if instr_n == 0:
            if instr.startswith('addx '):
                _, n_s = instr.split()
                x += int(n_s)



    advent.submit_answer(1, interesting_sums)



def part02(s):
    pixels = set()

    x = 1
    lines = iter(s.splitlines())
    instr_n = 0
    instr = 'noop'

    for i in range(1, 240 + 1):
        if instr_n == 0:
            instr = next(lines)
            if instr == 'noop':
                instr_n = 1
            elif instr.startswith('addx '):
                instr_n = 2

        instr_n -= 1

        if x - 1 <= ((i - 1) % 40) <= x + 1:
            pixels.add(((i - 1) % 40, (i - 1) // 40))

        if instr_n == 0:
            if instr.startswith('addx '):
                _, n_s = instr.split()
                x += int(n_s)

    return format_coords_hash(pixels).replace(' ', '.')

def format_coords_hash(coords: set[tuple[int, int]]) -> str:
    min_x = min(x for x, _ in coords)
    max_x = max(x for x, _ in coords)
    min_y = min(y for _, y in coords)
    max_y = max(y for _, y in coords)
    return '\n'.join(
        ''.join(
            '#' if (x, y) in coords else ' '
            for x in range(min_x, max_x + 1)
        )
        for y in range(min_y, max_y + 1)
    )

if __name__ == "__main__":
    lines = download_input_data()
    parser = argparse.ArgumentParser()
    parser.add_argument('data_file', nargs='?', default=INPUT_TXT)
    args = parser.parse_args()

    with open(args.data_file) as f:
        print(part01(f.read()))
    with open(args.data_file) as f:
        print(part02(f.read()))
    timer_start()
