a = {"a":100,"b":21,"c":33,"x":11,"e":54}
v = list(a.items())
for i in range(len(v)):
    for j in range(len(v)-i-1):
        if v[j][1] > v[j+1][1]:
            v[j],v[j+1] = v[j+1],v[j]
print(dict(v))
