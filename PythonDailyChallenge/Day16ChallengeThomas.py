""" Day 16
Given an integer n, find all the integers that is the multiple of 3 from 0 to n. Return the sum of all these integers.



Example:

Input: 

10

Multiples of 3 from 0 to 10:

3, 6, 9

Return sum of these integers:

18 """

x = 10
#x=20
#x = 40
su=0
for i in range (0,x+1):
    if i % 3 ==0:
        su = i + su
print(su)