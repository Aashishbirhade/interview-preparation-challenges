arr = [3,5,1,9,7]
mi = arr[0]
ma = arr[0]
for i in arr:
    if mi >= i:
        mi = i
    if ma <= i:
        ma = i
    
print("minimum element is: ", mi, "and maximum is :", ma)