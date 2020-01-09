z=[]
#x = "abcdefg"
x = "abcdef"
y = round(len(x) /2)
check = len(x) % 2

for i in range(y):
    
    if (check == 0 ):
        z.append(x[(2*i):((2*i)+2)])
    
    elif (i != y-1 and check == 1 ):
        z.append(x[(2*i):((2*i)+2)])
    
    elif(i == y-1 and check ==1):
        m = x[-1]+"?"
        z.append(m)
        
print(f"result {z}")