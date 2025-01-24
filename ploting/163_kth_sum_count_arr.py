a = [1,2,3,1,1,1]
k  = 3
c = 0
for i in range(len(a)):
    sami = 0
    for j in range(i,len(a)):
        sami += a[j]
        if sami == k:
            c += 1
print(c)