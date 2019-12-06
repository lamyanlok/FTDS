#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the compareTriplets function below.
def compareTriplets(a, b):
    a_score = 0
    b_score = 0
    c = []
    if a[0] > b[0]:
        a_score += 1
    elif b[0] > a[0]:
        b_score += 1

    if a[1] > b[1]:
        a_score += 1
    elif b[1] > a[1]:
        b_score += 1

    if a[2] > b[2]:
        a_score += 1
    elif b[2] > a[2]:
        b_score += 1
    c = [a_score,b_score]
    return c

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
