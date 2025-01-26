a = [2,0,1,2,1,0]
mi = 0
for i in range(len(a)):
    mi = i
    for j in range(i,len(a)):
        if a[mi] > a[j]:
            mi = j
    a[mi],a[i] = a[i],a[mi]
print(a)