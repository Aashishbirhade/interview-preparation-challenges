a = [32,4,3,66,87,44]
b = 2
for i in range(b):
    for j in range(len(a)-1,0,-1):
        a[j],a[j-1] = a[j-1],a[j]
print(a)