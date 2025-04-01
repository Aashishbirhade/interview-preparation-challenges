def isprime(a):
    f = 0
    for i in range(2,a):
        if a%i == 0:
            f = 1
            return f
    return f
a = 100
su = []
for i in range(2,a):
    v = isprime(i)
    if v == 0:
        su.append(i)
print(su)