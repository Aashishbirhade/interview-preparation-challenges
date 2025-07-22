a =10
n = a*(a+1)//2
for i in range(6):
    for j in range(i):
        print(n,end="   ")
        n -= 1
    print( )