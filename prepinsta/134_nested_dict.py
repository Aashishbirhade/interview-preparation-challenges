t = {'Gfg': {'a': 7, 'b': 9, 'c': 12},
             'is': {'a': 15, 'b': 19, 'c': 20},
             'best': {'a': 5, 'b': 10, 'c': 2}}
k = "a"
v  = []
for i in t.values():
    if k in i:
        v.append(i[k])
print(v)