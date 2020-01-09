#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the staircase function below.
def staircase(n):
    x = ' '
    y = '#'
    for i in range(n):
        s = (i+1)*y
        s = s.strip()
        u = (n-i-1)*x + s
        print(u)


if __name__ == '__main__':
    n = int(input())

    staircase(n)
