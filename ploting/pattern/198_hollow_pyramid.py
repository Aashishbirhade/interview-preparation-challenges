n = 5
for i in range(n+1):
    for k in range(n-i):
        print(" ",end=" ")
    for j in range(2*i+1):
        if j == 0 or i==n or j == 2*i:
            print("*",end=" ")
        else:
            print("-",end=" ")
    print("")