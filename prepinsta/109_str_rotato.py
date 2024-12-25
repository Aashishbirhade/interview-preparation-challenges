v ="Aashish"
a = list(v)
x  = 2
# for j in range(x):
#     for i in range(len(a)-1):
#         a[i],a[i+1] = a[i+1],a[i]
for i in range(x):
    for j in range(len(v)-1,0,-1):
        a[j],a[j-1] = a[j-1],a[j]
c = "".join(a)
print(c,v[1:])