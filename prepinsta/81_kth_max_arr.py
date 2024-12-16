a = [12, 3, 4, 22, 5, 7, 65]
k = 2
for _ in range(2):  
    ma = a[0]  
    for j in a: 
        if ma <= j:
            ma = j
    a.remove(ma)  
print(ma)  
