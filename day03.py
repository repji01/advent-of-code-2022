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
    global lines
    advent.setup(2022, 3, dry_run=False)
    fin = advent.get_input()
    lines = get_lines(fin.readlines())
    #lines = get_lines(xxx)
    return lines




def part01(lines):
    value = 0
    for line in lines:
        size = int(len(line)/2)

        items = [line[:size],line[size:]]
        itemX=''
        for item in items[0]:
            if item in items[1]:
                itemx = item
        if itemx.isupper():
            value += ord(itemx) - 64 + 26
        else:
            value += ord(itemx) - 96


    advent.submit_answer(1, value)

def part02(lines):
    value = 0
    for idx in range(int(len(lines) / 3)):
        items = [lines[3*idx], lines[3*idx+1], lines[3*idx+2]]
        itemX = ''
        for item in items[0]:
            if (item in items[1]) and (item in items[2]):
                itemx = item
        if itemx.isupper():
            value += ord(itemx) - 64 + 26
        else:
            value += ord(itemx) - 96
    advent.submit_answer(2, value)



if __name__ == "__main__":
    lines = download_input_data()
    timer_start()

    part01(lines)
    part02(lines)

