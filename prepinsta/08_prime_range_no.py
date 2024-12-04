def primerange(n):
    f = True
    for i in range(2,n):
        if n%i == 0:
            f = False
            return f
    return f


n = 100
for i in range(1,n):
    v = primerange(i)
    if v:
        print(i ,end=" ")