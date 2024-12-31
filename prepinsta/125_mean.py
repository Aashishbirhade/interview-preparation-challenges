a = {"a":100,"b":21,"c":33,"x":11,"e":21}
print(len(a))

s = 0
for i in list(a.values()):
    s += i
print(s/len(a))