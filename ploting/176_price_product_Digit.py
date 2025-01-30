a = 234
p = 1
while a!=0:
    rem = a%10
    p *= rem
    a //= 10
print(p)