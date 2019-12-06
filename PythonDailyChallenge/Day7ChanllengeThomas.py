x = [2,2,2,2,2,2,2,3]
for i in x:
    if x.count(i) != 1:
        continue
    elif x.count(i) == 1:
        result = i
print(i)