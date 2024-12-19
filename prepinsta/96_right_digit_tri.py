a = 5
for i in range(a+1):
    for j in range(a-i):
      print(" ",end=" ")
    for j in range(i):
        print("*",end=" ")
    print()