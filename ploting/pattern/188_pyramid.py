n = 5
for i in range(n):
    for k in range(n-i):
        print(" ",end=" ")
    for k in range(2*i+1):
        print("*",end=" ")
    print(" ")
    