a = 99
r = 3
su = 0
while a!= 0:
    rem = a%10
    su += rem
    a //= 10
su *= r
su1 =0
while su!= 0:
    rem = su%10
    su1 += rem
    su//= 10
print(su1)