b = 4
c = 65
d = 65
for i in range(b+1):
    for k in range(b-i):
        print(" ",end=" ")
    for j in range(2*i+1):
        print(chr(c),end=" ")
    c += 1
    print(" ")
for i in range(b-1,-1,-1):
    for k in range(b-i):
        print(" ",end=" ")
    for j in range(2*i+1):
        print(chr(d),end=" ")
    d += 1
    print(" ")