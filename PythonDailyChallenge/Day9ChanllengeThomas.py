x = "2minus6plus4plus7"
#x = "1plus2plus3minus4"
y = x.split("plus")

sum = 0
for i in y:
    if i.isdigit():
        sum = sum+ int(i)
    if "minus" in i:
        z = i.split("minus")
        
        for num,j in enumerate (z,start = 1):
            if num == 1:
                minus = int(j)
            else:
                minus = minus - int(j)
    
result = sum + minus
print(result)