#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'getTotalX' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def getTotalX(a, b):
    # Write your code here
    small = b[0]
    for j in range(0,m):
        if b[j] < small:
            small = b[j]
    temp1=[]
    for k in range(1,small+1):
        for i in range(0,n):
            if (k % a[i] ==0):
                temp1.append(k)

    resulta = []
    resulta = list(set([x for x in temp1 if temp1.count(x) >= n]))

    temp2=[]
    for i in resulta:
        for j in range(0,m):
            if b[j] % i ==0:
                temp2.append(i)
            

    resultb = []
    resultb = list(set([x for x in temp2 if temp2.count(x) >= m]))

    return(len(resultb))  


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)

    fptr.write(str(total) + '\n')

    fptr.close()
