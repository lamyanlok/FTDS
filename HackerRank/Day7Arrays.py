import numpy

def arrays(arr):
    # complete this function
    # use numpy.array
    a = []
    b = numpy.array(arr,float)
    a = b[::-1]
    return a

arr = input().strip().split(' ')
result = arrays(arr)
print(result)