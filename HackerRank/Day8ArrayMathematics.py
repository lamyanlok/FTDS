import numpy
n, m = input().split()
my_arr = []
bmy_arr=[]
for i in range(int(n)):
    arr = input().strip().split(' ')
    arr = list(map(int, arr))
    my_arr.append(arr)
a = numpy.array(my_arr,int)

for i in range(int(n)):
    barr = input().strip().split(' ')
    barr = list(map(int, barr))
    bmy_arr.append(barr)
b = numpy.array(bmy_arr, int)

print (numpy.add(a, b))
print (numpy.subtract(a, b))
print (numpy.multiply(a, b))
print (numpy.floor_divide (a, b)) 
print (numpy.mod(a, b))
print (numpy.power(a, b))