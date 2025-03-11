v = 5
for i in range(v+1):
    for j in range(v-i):
        print(" ",end=" ")
    for k in range(4*i):
        print("*",end=" ")
    print(" ")