""" Day 18 Given an integer greater than 0, return a list of all possible palindromes of the integer.

Example:

Input:

34322122

Output:

[22, 212, 343, 22122] """

result = []
x = 34322122
sx = str(x)
l = len(sx)
for i in range (l-1):
    for j in range (i+1,l):
        if sx[i] == sx[j]:
            diff = j - i
            hit = sx[i:i+diff+1]
            if diff < 3:
                result.append(hit)

            if diff >=3:
                z = diff -2
            
                for k in range(1,z):
                    if sx[i+k] == sx[j-k]:
                    
                        result.append(hit)
            

tresult = list(set(result))
print(f'result {tresult}')