a = [1,2,31,5,3,7]
ma = a[0]
for i in a:
    if ma <= i:
        ma = i
print("Maximum:",ma)