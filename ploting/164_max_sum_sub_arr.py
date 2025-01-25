a = [-2,1,-3,4,-1,2,1,-5,4]
m = 0
su = 0
for i in a:
    su += i
    if su < 0:
        su = 0
    m = max(su,m)
print(m)