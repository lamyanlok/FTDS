#x = "9"
#x = 529
#x = 20
x = 15
y = bin(int(x))[2:]
z = str(y)
pos = []
for num,i in enumerate (z,start=1):
    if i == "1":
        pos.append(num)
    
end = len(pos)
diff=[]
for y in range(end-1):
    cal = pos[end-1-y] - pos[end-2-y]-1
    diff.append(cal)
maxi = 0
for j in diff:
    if j > maxi:
        maxi = j
print(maxi)