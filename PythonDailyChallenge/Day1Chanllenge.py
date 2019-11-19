string = 'In a trimmed estimator, the extreme values are discarded; '
new_string = []
for i in string:
    if i.islower():
        new_string.append(i)
    elif i.isalnum == False:
        new_string.append(i)
    elif i == ' ':
        new_string.append(i)

string_join = ''.join(new_string)

print(string_join)