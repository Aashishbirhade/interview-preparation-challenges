a = [1, 3, -1, 4, -3, -5, -6, 3, 7]
for i in range(len(a)):
    for j in range(len(a)-i-1):
        if a[j] > a[j+1]:
            a[j+1],a[j] = a[j],a[j+1]
print(a)