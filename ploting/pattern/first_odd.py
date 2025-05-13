def frequency(a):
    dict = {}
    for i in a:
        if i in dict:
            dict[i] += 1
        else:
            dict[i] = 1
    return dict
n = 7
a = ['a','b','b','b','c','c','c','a','f','c'] 
v = frequency(a)
print(v)
for key, value in v.items():
    if value % 2 != 0:
        print(f"First odd-count key: '{key}' with count {value}")
        break