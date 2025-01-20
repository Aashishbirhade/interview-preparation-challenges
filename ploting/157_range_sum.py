a = [1, 0, 1, 1,0, 1]
k = 0
ma = 0
for i in a:
    if i == 1:
        k+= 1
    else:
        k = 0
    ma = max(k,ma)
print(ma)