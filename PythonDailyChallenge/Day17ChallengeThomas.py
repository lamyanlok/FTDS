""" Day17
Given a list of 11 integers, return a string in the form of a Hong Kong phone number in this format: +852 xxxx xxxx

Only the numbers 2, 3, 5, 6, 7, and 9 can be added after the extension 852.



Example 1:

Input:

[1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1]

Returns:


"+852 9134 6701" """

import random

num =[]
first = [2,3,5,6,7,9]
one = (random.choice(first))
number = [0,1,2,3,4,5,6,7,8,9]
for i in range (7):
    temp = (random.choice(number))
    num.append(temp)
result = '+852'+' '+str(one)+str(num[0])+str(num[1])+str(num[2])+' '+str(num[3])+str(num[4])+str(num[5])+str(num[6])
print(result)