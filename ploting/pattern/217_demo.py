c = 5
a = 65
for i in range(c+1):
    for j in range(i):
        print(chr(a),end=" ")
        a += 1
    print(" ")