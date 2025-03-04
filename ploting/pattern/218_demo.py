n = 6
for i in range(n+1):
    for j in range(n+1):
        if j == 0 or j == n or i == 0 or i==n or i== n//2:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print(" ")
