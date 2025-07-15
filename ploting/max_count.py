n = 6
a = [5,6,3,7,2,10]
maxi = a[0]
c = 1
for i in (1,a):
    if (maxi<i): 
        maxi = i
        c += 1
print("count of maximum",c)
