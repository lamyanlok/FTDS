import numpy
inpu = [1,2,3,4,5,6,7]
#inpu = [1,2,3,4,5,6]
l = len(inpu)

if l % 2 ==1:
    first = int((l-1) /2)
    x = inpu[0:first]
    y = inpu[first:l]
    x.insert(first,0)
elif l %2 ==0:
    first = int((l) /2)
    x = inpu[0:first]
    y = inpu[first:l]

x=numpy.array(x)
y=numpy.array(y)
result = x+y
print(result)