""" Given two lists of any data type, return a list that combines the two lists by alternating the elements passed. The input lists can be of different lengths.



Example 1:

Input lists: 

[1, 2, 3, 4, 5]

['a', 'b', 'c', 'd', 'e']

Returns:

[1, 'a', 2, b', 3, 'c', 4, 'd', 5, 'e']



Example 2:

Input lists:

[1, 2, 3]

['a', 'b', 'c', 'd', 'e']

Returns:

[1, 'a', 2, 'b', 3, 'c', 'd', 'e']



Example 3:

Input lists:

[1, 2, 3, 4, 5]

['a', 'b']

Returns:

[1, 'a', 2, 'b', 3, 4, 5] """

#x = [1, 2, 3, 4, 5]
#y = ['a', 'b', 'c', 'd', 'e']
#x = [1, 2, 3]
#y = ['a', 'b', 'c', 'd', 'e']
x =[1, 2, 3, 4, 5]

y =['a', 'b']

xl = len(x)
yl = len(y)

z=[]

if xl<=yl:
    for i in range(0,xl):
        z.append(x[i])
        z.append(y[i])
    z.extend(y[xl:yl])
    
if xl>yl:
    for i in range(0,yl):
        z.append(x[i])
        z.append(y[i])
    z.extend(x[yl:xl])

print(z)