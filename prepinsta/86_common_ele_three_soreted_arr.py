a = [1,2,3,4,5,6]
b = [1,3,5,7,9,11]
c = [2,4,5,6,8,10]
for i in range(len(a)):
    if a[i] in b  and a[i] in c:
        print(a[i],end = " ")
