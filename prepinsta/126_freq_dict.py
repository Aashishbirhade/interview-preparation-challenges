def frequency(x):
    c = 0
    for i,j in a.items():
        if x == j:
            c += 1
    return c
a = {"a":100,"b":21,"c":33,"x":11,"e":21}
for i,val in a.items():
    v = frequency(val) 
    print(v,end=" ")