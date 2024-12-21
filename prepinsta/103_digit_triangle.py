a = 5
for i in range(a):
    for j in range(i):
        i += 2
        print(i,end=" ")
    for j in range(a-i):
        print(" ",end=" ")
    print()