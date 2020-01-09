def middle(x):
    y = x.split()
    z = len(y)
    if z % 2 == 1:
        u = int((z-1) /2)
        middle_string = y[u]
    if z % 2 == 0:
        u = int(z /2)
        middle_string = str(y[u-1]) + ' '+str(y[u])

    return middle_string

x = input("Pls input your string.")
result = middle(x)

print(result)