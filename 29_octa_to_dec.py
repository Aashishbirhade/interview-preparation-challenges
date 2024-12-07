a  = int(input("enter any octa no: "))
if a<=7:
    print(f"decimal form of given no is as it {a}")
else:
    sa = 0
    c = 0
    while a!=0:
        rem  = a%10
        if rem == 8:
            print(f"invalid input for octa {a} contain 8")
            break
        else:
            sa += rem *(8**c) # base 8^0 ,01234
            a //= 10
            c +=1
    print(f"given octa no  convert into dec:{sa}") 