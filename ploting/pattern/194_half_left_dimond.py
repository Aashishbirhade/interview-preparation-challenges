n = 5
for i in range(n+1):
    for k in range(n-i):
        print(" ",end=" ")
    for j in range(i):
        if j <= (n+1)//2:
            print("*",end=" ")
    print(" ")
for i in range(n-1,0,-1):
    for j in range(n-i):
        print(" ",end=" ")
    for k in range(i):
        if j <= (n+1)//2:
            print("*",end=" ")
    print(" ")
