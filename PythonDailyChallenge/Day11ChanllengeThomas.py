s = "acdbcd"
d = {i: s.rfind(i) - s.find(i) for i in sorted(set(s)) if s.count(i)>1}
result = max(d,key=d.get)
print(result)