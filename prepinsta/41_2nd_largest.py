a = [3,5,1,9,7]
ma = a[0]
sa = a[0]
for i in a:
    if ma <= i:
        ma =i
for i in a :
    if sa < i and i < ma :
        sa = i
print(ma,sa)