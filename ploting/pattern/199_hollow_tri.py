n = 6
for i in range(n+1):
    for j in range(i):
        if j == 0 or i == 6 or  j == i-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()