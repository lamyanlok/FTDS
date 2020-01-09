def sum_cubes(n):
    sum = 0
    x = 0
    for i in range(n):
        x = (i+1) * (i+1) *(i+1)
        sum += x
    
    return sum

n = int(input("Pls enter a positive integer"))
print(sum_cubes(n))