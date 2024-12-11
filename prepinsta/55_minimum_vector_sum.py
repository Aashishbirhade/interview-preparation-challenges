a = [1, 2, 6, 3, 7]
b = [10, 7, 45, 3, 7]
for i in range(len(a)):
    for j in range(len(a)-i-1):
        if a[j]> a[j+1]:
            a[j],a[j+1] = a[j+1],a[j]
sami = 0
for i in range(len(b)):
    for j in range(len(b)-i-1):
        if b[j]< b[j+1]:
            b[j],b[j+1] = b[j+1],b[j]
for i in range(len(a)):
    sami += (a[i]*b[i])
print(sami)