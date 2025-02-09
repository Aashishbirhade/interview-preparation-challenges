n = 12
k =2
c = 0
for  i in range(n,0,-1):
    if n%i == 0:
        if c == k:
            print(i,end=" ")
        c += 1
    
