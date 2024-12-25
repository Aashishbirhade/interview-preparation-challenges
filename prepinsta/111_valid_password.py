a = "Aashish123"
l,u,d,p = 0,0,0,0
if len(a)>= 8:
    for i in a:
        if i.islower():
            l += 1
        elif i.isupper():
            u+= 1
        elif i.isdecimal():
            d+= 1
        else:
            p+=1
    if l>=1 and u>=1 and d>= 1 and p>=1 and l+u+d+p == len(a):
        print("Valid Password")
    else:
        print("Invalid passsword")
else:
    print("less 8 count")