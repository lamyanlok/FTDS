""" Day 22

Given a string of decimal digits, output an integer of its binary representation like below:



Example:

Input: "2973"

"2" => 10

"9" => 1001

"7" => 111

"3" => 11

Therefore output is 10100111111, because of 10+1001+111+11. """

x = "2973"
l = []
for i in x:
    y = bin(int(i))[2:]
    l.append(y)
s = ''.join(l)
print(s)