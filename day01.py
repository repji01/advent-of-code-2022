#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""day01.py: Advent of Code 2022 --- Day 2: Calorie Counting ---
   https://adventofcode.com/2022/day/1
"""

__version__ = "1.0"
__maintainer__ = "Jiří Řepík"
__email__ = "jiri.repik@gmail.com"
__status__ = "Submited"

import advent
from utils import *

def download_input_data():
    global fin
    global lines
    advent.setup(2022, 1, dry_run=False)
    fin = advent.get_input()
    lines = get_lines(fin.readlines())


def part01():
    global lines
    elf_total = 0
    elf_total_max = 0
    for line in lines:
        if len(line)>0:
            elf_total += int(line)
        else:
            if elf_total > elf_total_max:
                elf_total_max = elf_total
            elf_total = 0
    advent.submit_answer(1, elf_total_max)



def part02():
    global lines
    elf_total = 0
    elves = list()
    for line in lines:
        if len(line) > 0:
            elf_total += int(line)
        else:
            elves.append(elf_total)
            elf_total = 0
    elves.sort()
    advent.submit_answer(2, sum(elves[-3:]))



if __name__ == "__main__":
    download_input_data()
    timer_start()
    part01()
    part02()