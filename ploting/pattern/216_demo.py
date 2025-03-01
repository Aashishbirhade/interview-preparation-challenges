b = 4
c = 65
for i in range(b+1):
    c = 65
    for j in range(b+1):
        print(chr(c),end=" ")
        if j>= i:
            c += 1
    print(" ")