a = [18,34,2,5,6,33,56,74]
for i in range(len(a)):
    min = i
    for j in range(i,len(a)):
        if a[min] > a[j]:
            min = j
    a[i],a[min] = a[min],a[i]
print(a)