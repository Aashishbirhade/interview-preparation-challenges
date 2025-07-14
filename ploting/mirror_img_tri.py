n = 4
a =1

for i in range(n-1,0,-1):
    for j in range(n-i):
        print(" ",end=" ")
    for j in range(2*i-1):
        print(a,end=" ")
        a += 1
    print()

    