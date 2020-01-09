#!/bin/python3

import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    #
    # Write your code here.
    #
    x = s[-2:]
    hour = s[0:2]
    rest = s[2:-2]
    n_hour = int(hour)
    if x =="AM" and hour !="12":
        n_hour = str(hour)
    elif x == "PM" and hour == "12":
        n_hour = str(hour)
    elif x == "PM" and hour != "12":
        n_hour = int(hour) + 12
    elif x == "AM" and hour =="12":
        n_hour = str("00")
    result = str(n_hour)+rest
    return result

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()
