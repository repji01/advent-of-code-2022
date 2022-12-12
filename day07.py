#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""day05.py: Advent of Code 2022 --- Day 7: Rucksack Reorganization ---
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
from utils import *


def download_input_data():
    global fin
    advent.setup(2022, 7, dry_run=False)
    fin = advent.get_input()
    lines = fin.read()
    return lines

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

MAX = 100000
TOTAL = 70000000
NEED = 30000000

def part01(lines):
    total = 0
    pwd = '/'
    files = {}
    dirs = {'/':{}}
    in_ls = False

    for line in lines.splitlines()[1:]:
        if in_ls  and line.startswith('$'):
            in_ls = False
        if in_ls and line.startswith('dir'):
            _, dirname = line.split(' ',1)
            dirs.setdefault(os.path.join(pwd, dirname), {})
            continue
        elif in_ls:
            sz , filename = line.split(' ', 1)
            files[os.path.join(pwd, filename)] = int(sz)
            continue

        if line == '$ ls':
            in_ls = True
        elif line == '$ cd ..':
            pwd = os.path.dirname(pwd) or '/'
        elif line.startswith('$ cd'):
            pwd = os.path.join(pwd, line.split(' ', 2)[-1])
        else:
            AssertionError(line)

    def size(dirname):
        sz = 0
        for k,v in (files.items()):
            if k.startswith(f'{dirname}/'):
                sz += v
        if sz > MAX:
            return 0
        else:
            return sz

    root = sum(files.values())
    if root > MAX:
        root = 0


    return root + sum(size(dirname) for dirname in dirs)


    # advent.submit_answer(1, i + 1)



def part02(lines):
    total = 0
    pwd = '/'
    files = {}
    dirs = {'/': {}}
    in_ls = False

    for line in lines.splitlines()[1:]:
        if in_ls and line.startswith('$'):
            in_ls = False
        if in_ls and line.startswith('dir'):
            _, dirname = line.split(' ', 1)
            dirs.setdefault(os.path.join(pwd, dirname), {})
            continue
        elif in_ls:
            sz, filename = line.split(' ', 1)
            files[os.path.join(pwd, filename)] = int(sz)
            continue

        if line == '$ ls':
            in_ls = True
        elif line == '$ cd ..':
            pwd = os.path.dirname(pwd) or '/'
        elif line.startswith('$ cd'):
            pwd = os.path.join(pwd, line.split(' ', 2)[-1])
        else:
            AssertionError(line)

    def size(dirname):
        sz = 0
        for k, v in (files.items()):
            if k.startswith(f'{dirname}/'):
                sz += v
        return sz

    root = sum(files.values())


    sizes = [root] + [size(dirname) for dirname in dirs]
    sizes.sort()
    need_to_delete = NEED - (TOTAL - root)
    sizes2 = [size for size in sizes if size >= need_to_delete]
    sizes2.sort()
    print(sizes2)
    return root + sum(size(dirname) for dirname in dirs)


if __name__ == "__main__":
    lines = download_input_data()
    timer_start()

    print(part01(lines))
    print(part02(lines))
