a = {"a":100,"b":21,"c":33,"x":11,"e":21}
v = list(a.items())
for i in range(len(v)):
    for j in range(i+1,len(v)):
        if v[i][1] == v[j][1]:
            print(v[i][0],v[i][1])

