a = [1, 2, 4, 5, 7, 8, 3]
for i in range(1,len(a)):
    if a[i-1] < a[i] > a[i+1]:
        print(a[i])
