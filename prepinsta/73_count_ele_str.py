def isfrequency(i):
    c = 0
    for j in a:
        if i == j:
            c += 1
    return c
a = "aashish"
v  = a

for i in v:
    v = isfrequency(i)
    print(i , v,end = " ")