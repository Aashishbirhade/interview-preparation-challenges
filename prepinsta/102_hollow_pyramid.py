a = 5
for i in range(a):
    for j in range(a - 1 - i):
        print(" ", end=" ")  
    for j in range(2 * i + 1):
        if j == 0 or j == 2 * i or i == a-1:
            print("*", end=" ")
        else:
            print(" ", end=" ")  
    print() 
