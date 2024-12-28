a = {"aashish":1,"veer":2,"raaj":3,"ayush":5,"akhil":4}
print(a.values())
print(a.items())
v = list(a.items())
for i in range(len(v)):
    for j in range(len(v)-i-1):
        if v[j][0] > v[j+1][0]:
            v[j],v[j+1] = v[j+1],v[j]
print(dict(v)) 
