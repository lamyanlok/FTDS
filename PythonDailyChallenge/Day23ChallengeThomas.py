""" Day 23

Given an input integer x, return a list of integers in which the sum is equal to x. The integers must consist of values that are a power of 3. For example:

1 is a possible number of the list because of 3^0 => 1

3 is also a possible number of the list because 3^1 => 3

and so on """

x = 9
test =0
temp = x
result = []

for i in range (5):
    print(pow(3,i))
    test = pow(3,i)
    if temp > test:
        print(f"temp {temp}, test {test}")
        temp = temp - test
        result.append(test)
    if temp < test:
        print(f"temp {temp}, test {test}")
        result.append(temp)
        break

print(result)