#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countApplesAndOranges function below.
def countApplesAndOranges(s, t, a, b, apples, oranges):
    a_count = 0
    o_count = 0
    for i in apples:
        if (a + i) >= s and (a+i) <= t:
            a_count += 1
    for i in oranges:
        if (b + i) >= s and (b + i) <=t:
            o_count += 1
    print(a_count)
    print(o_count)

    return

if __name__ == '__main__':
    st = input().split()

    s = int(st[0])

    t = int(st[1])

    ab = input().split()

    a = int(ab[0])

    b = int(ab[1])

    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)