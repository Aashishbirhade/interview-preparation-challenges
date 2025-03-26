a = 5
for i in range(a+1):
    for j in range(a-i):
        print(" ",end = " ")
    for k in range(2*i+1):
        if i%2==0:
            print("*",end=" ")
        else:
            print("|",end=" ")

    print(" ")