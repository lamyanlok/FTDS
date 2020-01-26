#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the breakingRecords function below.
def breakingRecords(scores):
    in_min = scores[0]
    in_max = scores[0]
    count_min=0
    count_max=0
    out = []

    for i in range(1,n):
        if scores[i] < in_min:
            in_min = scores[i]
            count_min +=1
        if scores[i] > in_max:
            in_max = scores[i]
            count_max +=1

    
    out.append(count_max)
    out.append(count_min)

    return out

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
