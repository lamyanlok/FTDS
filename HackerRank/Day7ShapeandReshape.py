import numpy

arr = input().strip().split(' ')
arr = list(map(int, arr))

my_array = numpy.array(arr)
print (numpy.reshape(my_array,(3,3)))