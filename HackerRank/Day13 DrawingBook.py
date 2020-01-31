#!/bin/python3

import os
import sys

#
# Complete the pageCount function below.
#
def pageCount(n, p):
    #
    # Write your code here.
    #
    total=0
    d_total=0
    result=0


    if n %2 ==0:
        total = n+n+1
    
    if n %2 ==1:
        total = n+n-1
    
    if p %2 ==0:
        d_total = p+p+1

    if p %2 ==1:
        d_total = p+p-1
    
    if d_total >=total:
        presult = int((d_total - total) / 4)
    
    elif d_total < total:
        presult = int((total - d_total) / 4)

    fresult = int((d_total - 1)/4)
    
    if fresult <= presult:
        result = fresult
    elif fresult > presult:
        result = presult
    
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    p = int(input())

    result = pageCount(n, p)

    fptr.write(str(result) + '\n')

    fptr.close()
