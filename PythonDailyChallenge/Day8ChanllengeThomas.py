n = int(input("Pls input number n"))
d = input("Pls input number d")
result = 0
for i in range (1,n+1):
    times = i*i
    check = str(times)
    for j in check:
        if d == j:
            result += 1
        

print(result)