#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""day09.py: Advent of Code 2022 --- Day 3: Rucksack Reorganization ---
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


class Snake():

    def __init__(self, head, tail, start_position, grid_size):
        self.head = head
        self.tail = tail
        self.start_position = start_position
        self.grid = {(x, y): ' ' for x in range(-grid_size, grid_size) for y in range(-grid_size, grid_size)}

    def move(self, instruction):
        #move head
        direction, amount = instruction.split()
        amount = int(amount)
        for _ in range(amount):
            head_x, head_y = self.head
            if direction == 'R':
                head_y += 1
            if direction == 'L':
                head_y -= 1
            if direction == 'U':
                head_x -= 1
            if direction == 'D':
                head_x += 1
            self.head = (head_x, head_y)
            self.fix_tail()
            #print(self.print_grid())



    def fix_tail(self):
        head_x, head_y = self.head
        tail_x, tail_y = self.tail
        self.grid[self.tail] = '#'
        if abs(self.head[0] - self.tail[0]) >= 2 or abs(self.head[1] - self.tail[1]) >= 2:
            if self.head[0] > self.tail[0]:
                tail_x += 1
            if self.head[0] < self.tail[0]:
                tail_x -= 1

            if self.head[1] > self.tail[1]:
                tail_y += 1
            if self.head[1] < self.tail[1]:
                tail_y -= 1
            self.tail = (tail_x, tail_y)

    def print_grid(self):
        gridx = self.grid
        x_max, y_max = max(gridx)
        x_min, y_min = max(gridx)
        s = ''
        s = str(self.grid)
        """
        for x in range(x_min, x_max):
            for y in range(y_min, y_max ):
                position = (x,y)
                c = str(gridx[x, y])
                if position == self.start_position:
                    c = 'S'
                if position == self.tail:
                    c = 'T'
                if position == self.head:
                    c = 'H'
                s += c
            s += '\n'"""
        return s

    def count_tale_position(self):
        count = 0
        x_max, y_max = max(self.grid)
        s = ''

        for x in range(x_max + 1):
            for y in range(y_max + 1):
                if self.grid[x,y] == '#':
                    count +=1
        return count

def download_input_data():
    global fin
    advent.setup(2022, 9, dry_run=False)
    fin = advent.get_input()
    lines = get_lines(fin.readlines())
    return lines

TEST_LINES = """R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2""".split('\n')


def part01(lines):
    #init grid
    n = m = 5
    snake = Snake((0,0), (0,0), (0,0), 150)

    for line in lines:

        direction, move = line.split()
        snake.move(line)

    print(str(snake.grid))
    print(snake.count_tale_position())
    pass



def part02(lines):
   pass



if __name__ == "__main__":
    lines = download_input_data()
    timer_start()

    print(part01(lines))
    print(part02(lines))
