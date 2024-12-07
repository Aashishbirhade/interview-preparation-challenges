a = int(input("enter any bineary no : "))
su = 0
c = 0
while a!=0:
    rem = a%10
    if rem == 1 or rem ==0:
        su += rem*(2**c)
        a//= 10
        c +=1
    else:
        print("Unexpexted Input pass user")
        break
print(su)

