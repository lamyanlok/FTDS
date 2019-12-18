import numpy
#arr = input().strip().split(' ')
#arr = list(map(int,arr))
#n = arr[0]
#m = arr[1]
#print(numpy.eye(n,m))

n, m = input().split()

numpy.set_printoptions(sign=' ') 
print(numpy.eye(int(n), int(m)))