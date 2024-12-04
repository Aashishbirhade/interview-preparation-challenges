n = int(input("Enter the number :"))
flag = True
if n == 0 or n == 1:
    flag = False
else:
    for i in range(2, n//2):
        if n % i == 0:
            flag = False
            break
if flag == False:
    print("It is not prime")
else:
    print("It is a prime number")