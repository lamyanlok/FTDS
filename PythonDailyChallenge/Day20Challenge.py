""" Day20 Given a string, count all the lowercase letters. Return a dictionary with the keys as the lowercase letters and the values as the letters' counts respectively. The keys should be sorted in alphabetical order.

Example:

Input:

"apple"

Output:

{'a': 1, 'e': 1, 'l': 1, 'p': 2} """

x = "apple"
count_letters = {}
cnt_lowercase = 0
cnt_uppercase = 0
for c in x:
    if c.islower():
        if (c in count_letters) == False:
            count_letters[c]={c:x.count(c)}
            cnt_lowercase += 1
    if c.isupper():
        if (c in count_letters) == False:
            count_letters[c]={c:x.count(c)}
            cnt_uppercase += 1
count_letters = { k : v[k] for k, v in count_letters.items()}
print(count_letters)