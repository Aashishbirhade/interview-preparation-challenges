a = {"a":100,"b":21,"c":33,"x":11,"e":21}
k = "a"
rep = "s"
for i,j in list(a.items()):
    if i == k:
        a[rep] =  j
        a.pop(i)
print(a)