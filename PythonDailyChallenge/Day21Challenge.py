""" Day 21 Given a list of mixed integers of different representations, add up the non-string integers and subtract this from the total of string integers.

Example:

Input:

[1, '2', 3, '4', 5]

Output:

-3, because:

total of non-string integers = 1+3+5 = 9

total of string integers = 2+4 = 6

total of string integers - total of non-string integers = -3 """

x = [1, '2', 3, '4', 5]
int_sum=0
str_sum = 0
for i in x:
    if type(i) == int:
        int_sum += i
    if type(i) == str:
        str_sum += int(i)

print(str_sum - int_sum)