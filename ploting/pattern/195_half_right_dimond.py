n = 5
for i in range(n+1):
    for j in range(i):
        print("*",end=" ")
    for k in range(n-i):
        print(" ",end=" ")
    print(" ")
for i in range(n-1,0,-1):
    for j in range(i):
        print("*",end=" ")
    for k in range(n-i):
        print(" ",end=" ")
    print(" ")