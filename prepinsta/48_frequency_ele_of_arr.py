def frequency(i):
    c = 0
    for j in a:
        if i==j:
            c+=1
    return c


a =[10, 20, 30, 40, 40, 50, 50, 50]
for i in set(a):
    cou = frequency(i)
    print(f"{i}:{cou}")
