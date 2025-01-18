a = [7, 1, 5, 3, 6, 4]
max_value = 0

for i in range(len(a)):
    for j in range(i+1,len(a)):
        if a[j]>a[i]:
            max_value =  max(a[j]-a[i],max_value)
print("maximum Profit :",max_value)