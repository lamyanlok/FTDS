import numpy
arr = input().strip().split(' ')
arr = list(map(int, arr))
x = arr[0]
y = arr[1]
my_array = []
for i in range (x):
    arr = input().strip().split(' ')
    arr = list(map(int, arr))
    my_array.append(arr)
narray = numpy.array(my_array)

print (numpy.transpose(narray))
print (narray.flatten())