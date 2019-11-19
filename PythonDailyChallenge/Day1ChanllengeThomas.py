x = input("Pls input the text message.")
print(x)
y = []
for word in x:
    if word.islower():
        y.append(word)
    else:
        continue
print(y)
z = ''.join(y)
print(z)