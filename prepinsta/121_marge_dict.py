a = {"a":100,"b":21,"c":33,"x":11,"e":21}
b  = {"f":10,"h":221,"d":3}
1
# a.update(b)
# print(a)

2
# print(a|b)

3
for k,v in b.items():
    a[k] = v
print(a)