#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""day01.py: Advent of Code 2022 --- Day 2: Paper Scissors ---
   https://adventofcode.com/2022/day/2
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
    advent.setup(2022, 2, dry_run=False)
    fin = advent.get_input()
    lines = fin.read()


shape = {'R': 1, 'P': 2, 'S': 3}
win = {'R': 'S', 'P': 'R', 'S': 'P'}

def part01(s):
    trans = {
        'A': 'R', 'B': 'P', 'C': 'S',
        'X': 'R', 'Y': 'P', 'Z': 'S',
    }
    for k, v in trans.items():
        s = s.replace(k, v)

    n = 0
    for line in s.splitlines():
        a, b = line.split()
        if a == b:
            n += 3
        elif win[a] != b:
            n += 6
        else:
            pass
        n += shape[b]
    advent.submit_answer(1, n)

def part02(s):
    lose = {v: k for k, v in win.items()}
    trans = {'A': 'R', 'B': 'P', 'C': 'S'}

    for k, v in trans.items():
        s = s.replace(k, v)

    n = 0
    for line in s.splitlines():
        a, b = line.split()
        if b == 'X':
            n += shape[win[a]]
        elif b == 'Y':
            n += shape[a] + 3
        else:
            n += shape[lose[a]] + 6
    advent.submit_answer(2, n)



if __name__ == "__main__":
    download_input_data()
    timer_start()
    global lines
    part01(lines)
    part02(lines)

