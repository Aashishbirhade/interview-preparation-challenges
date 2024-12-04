a = 407
v = len(str(a))
sumi = 0
while a!= 0:
    rem = a%10
    sumi += rem**v
    a//=10
if sumi == a:
    print("given no is Armstrong no")
else:
    print("Given no is not Armstrong no")