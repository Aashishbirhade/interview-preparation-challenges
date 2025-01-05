test_dict = {'Gfg': {'a': 7, 'b': 9, 'c': 12},
             'is': {'a': 15, 'b': 19, 'c': 20},
             'best': {'a': 5, 'b': 10, 'c': 2}}
v = "a"
su = 0
for i in test_dict.values():
    if v in i:
        su += i[v]
print(f"sum of {v}:{su}")