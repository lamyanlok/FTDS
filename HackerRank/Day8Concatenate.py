import numpy
arr = input().strip().split(' ')
n = int(arr[0])
m = int(arr[1])
p = int(arr[2])
my_arr = []
for i in range(n+m):
    arr = input().strip().split(' ')
    arr = list(map(int, arr))
    my_arr.append(arr)
narray = numpy.array(my_arr)
print(narray)