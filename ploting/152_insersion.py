a = [12,53,2,42,6,4]
for i in range(len(a)):
    j = i
    while j> 0 and a[j-1] >a[j]:
        a[j-1],a[j] = a[j],a[j-1]
        j -= 1
print(a)