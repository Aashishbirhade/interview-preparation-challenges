a = 5
for i in range(a):
    for j in range(i):
        print(" ",end=" ")
    for j in range((2*a)-(2*i+1)):
        print("*",end=" ")
    print()