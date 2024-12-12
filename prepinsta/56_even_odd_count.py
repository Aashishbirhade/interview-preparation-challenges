a = [11, 20, 35, 40, 53]
c_even = 0
c_odd = 0
for i in a:
    if i %2==0:
        c_even += 1
    else:
        c_odd += 1
print(c_even,c_odd)