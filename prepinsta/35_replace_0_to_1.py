a = 13020 #13121
f =1
rev = 0
while a!=0:
    rem = a%10
    if rem == 0:
        rem = 1
    rev =  rev + rem*f
    f *= 10
    a//=10
print(rev)