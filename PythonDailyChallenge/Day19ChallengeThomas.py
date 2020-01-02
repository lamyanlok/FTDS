""" Day 19 Given a string of names with a certain pattern, return a formatted string with a certain pattern.

Example:

Input:

"Alfred:Black;Carey:Drake;Elena:Ferguson;Georgina:Harrison"

Output:

"(BLACK, ALFRED)(DRAKE, CAREY)(FERGUSON, ELENA)(HARRISON, GEORGINA)" """

x = "Alfred:Black;Carey:Drake;Elena:Ferguson;Georgina:Harrison"
y = x.split(";")

arr = []
for i in y:
    z = i.split(":")
    uz1 = z[1].upper()
    uz0 = z[0].upper()
    output = "("+uz1+","+uz0+")"
    arr.append(output)
    
sarr = ''.join(arr)
print(sarr)