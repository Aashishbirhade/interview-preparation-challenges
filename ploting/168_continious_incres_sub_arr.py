a = [2,5,6,3,25,3]
m = 0
c =  1
for i in range(len(a)-1):
    if  a[i] < a[i+1]:
        c += 1
    else:
        c = 0
    m = max(m,c)
print(m)