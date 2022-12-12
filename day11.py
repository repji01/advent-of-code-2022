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
import math
import os
from typing import NamedTuple, Callable

import advent
from utils import *


def download_input_data():
    global fin
    global lines
    advent.setup(2022, 11, dry_run=False)
    fin = advent.get_input()
    return fin.read()


def add(val: int, n: int) -> int:
    return val + n


def mult(val: int, n: int) -> int:
    return val * n


def square(val: int) -> int:
    return val * val


class Monkey(NamedTuple):
    items: list[int]
    fn: Callable[[int], int]
    mod: int
    true_target: int
    false_target: int

def part01(lines):
    monkeys = []
    for part in lines.split('\n\n'):
        monkey_lines = part.splitlines()
        starting = [int(s) for s in monkey_lines[1].split(': ')[1].split(', ')]
        if 'old * old' in monkey_lines[2]:
            fn = square
        elif ' + ' in monkey_lines[2]:
            fn = functools.partial(add, n=int(monkey_lines[2].split()[-1]))
        elif ' * ' in monkey_lines[2]:
            fn = functools.partial(mult, n=int(monkey_lines[2].split()[-1]))
        else:
            raise AssertionError(lines[2])
        mod = int(monkey_lines[3].split()[-1])
        true_target = int(monkey_lines[4].split()[-1])
        false_target = int(monkey_lines[5].split()[-1])
        monkeys.append(Monkey(starting, fn, mod, true_target, false_target))
    seen = [0] * len(monkeys)

    for _ in range(20):
        for i, monk in enumerate(monkeys):
            for item in monk.items:
                seen[i] += 1

                item = monk.fn(item) // 3
                if item % monk.mod == 0:
                    monkeys[monk.true_target].items.append(item)
                else:
                    monkeys[monk.false_target].items.append(item)

            monk.items.clear()

    seen.sort()
    advent.submit_answer(1, seen[-1] * seen[-2])

def part02(s):
    monkeys = []
    for part in s.split('\n\n'):
        monkey_lines = part.splitlines()
        starting = [int(s) for s in monkey_lines[1].split(': ')[1].split(', ')]
        if 'old * old' in monkey_lines[2]:
            fn = square
        elif ' + ' in monkey_lines[2]:
            fn = functools.partial(add, n=int(monkey_lines[2].split()[-1]))
        elif ' * ' in monkey_lines[2]:
            fn = functools.partial(mult, n=int(monkey_lines[2].split()[-1]))
        else:
            raise AssertionError(monkey_lines[2])
        mod = int(monkey_lines[3].split()[-1])
        true_target = int(monkey_lines[4].split()[-1])
        false_target = int(monkey_lines[5].split()[-1])
        monkeys.append(Monkey(starting, fn, mod, true_target, false_target))

    fac = math.prod(monk.mod for monk in monkeys)

    seen = [0] * len(monkeys)

    for j in range(10000):
        for i, monk in enumerate(monkeys):
            for item in monk.items:
                seen[i] += 1

                item = monk.fn(item) % fac
                if item % monk.mod == 0:
                    monkeys[monk.true_target].items.append(item)
                else:
                    monkeys[monk.false_target].items.append(item)

            monk.items.clear()

    seen.sort()
    advent.submit_answer(2, seen[-1] * seen[-2])



if __name__ == "__main__":
    lines = download_input_data()
    timer_start()
    part01(lines)
    part02(lines)

