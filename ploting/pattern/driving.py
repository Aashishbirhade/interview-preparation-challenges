n = 4
li = [5,2,3,7]
d = 12
x = 200
c = 0
for i in range(len(li)):
    if d%2==0:
        if li[i]%2!=0:
            c +=1
    
    else:
        if li[i]%2==0:
            c +=1
print(c*x)