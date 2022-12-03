#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Advent of Code 2012 --- execute all days ---
"""

__version__ = "1.0"
__maintainer__ = "Jiří Řepík"
__email__ = "jiri.repik@gmail.com"
__status__ = "Submited"


from utils import *
import os

from utils.helpers import timer_start

timer_start()
for day in range(1,25):
	if os.path.exists(f"day{str(day).zfill(2)}.py"):
		os.system(f"python3 day{str(day).zfill(2)}.py")