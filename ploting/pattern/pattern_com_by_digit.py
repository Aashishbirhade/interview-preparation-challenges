n = 6 
c = 0
for i in range(n):
    for j in range(i):
        print(c,end=" ")
    c += 1
    print()

for i in range(n-1,0,-1):
    for j in range(i):
        print(c,end=" ")
    c -= 1
    print()