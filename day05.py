#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""day05.py: Advent of Code 2022 --- Day 5: Supply Stacks ---
   https://adventofcode.com/2022/day/5
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
    advent.setup(2022, 5, dry_run=False)
    fin = advent.get_input()
    lines = fin.read()
    return lines


def part01(lines):
    first, rest = lines.split('\n\n')

    lastline_len = len(first.splitlines()[-1].rstrip())
    stacks: list[list[str]]
    stacks = [[] for _ in range((lastline_len + 2) // 4)]

    for line in first.splitlines():
        for i, c in enumerate(line[1::4]):
            if not c.isspace():
                stacks[i].append(c)

    for stack in stacks:
        stack.reverse()

    for instr in rest.splitlines():
        _, n_s, _, f_s, _, d_s = instr.split()
        n, f, d = int(n_s), int(f_s), int(d_s)

        for _ in range(n):
            stacks[d - 1].append(stacks[f - 1].pop())

    advent.submit_answer(1, ''.join(stack[-1] if stack else '' for stack in stacks))


def part02(lines):
    first, rest = lines.split('\n\n')

    lastline_len = len(first.splitlines()[-1].rstrip())
    stacks: list[list[str]]
    stacks = [[] for _ in range((lastline_len + 2) // 4)]

    for line in first.splitlines():
        for i, c in enumerate(line[1::4]):
            if not c.isspace():
                stacks[i].append(c)

    for stack in stacks:
        stack.reverse()

    for instr in rest.splitlines():
        _, n_s, _, f_s, _, d_s = instr.split()
        n, f, d = int(n_s), int(f_s), int(d_s)

        victims = stacks[f - 1][-n:]
        del stacks[f - 1][-n:]

        stacks[d - 1].extend(victims)

    advent.submit_answer(2, ''.join(stack[-1] if stack else '' for stack in stacks))


if __name__ == "__main__":
    lines = download_input_data()
    timer_start()

    part01(lines)
    part02(lines)
