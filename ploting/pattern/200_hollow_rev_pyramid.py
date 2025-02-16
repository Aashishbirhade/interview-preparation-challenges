n = 6
for i in range(n+1):
    for j in range(n-i):
        print(" ",end=" ")
    for k in range(i):
        if i == n or k == 0 or k== i-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print(" ")