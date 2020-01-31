#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the bonAppetit function below.
def bonAppetit(bill, k, b):
    total = 0
    split = 0
    for i in range(0,n):
        if i != k:
            total += bill[i]

    split = int(total / 2)

    if b != split:
        print (b-split)

    if b == split:
        print('Bon Appetit')

    return

if __name__ == '__main__':
    nk = input().rstrip().split()

    n = int(nk[0])

    k = int(nk[1])

    bill = list(map(int, input().rstrip().split()))

    b = int(input().strip())

    bonAppetit(bill, k, b)