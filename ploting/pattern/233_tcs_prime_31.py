import math
def isprime(a):
    f = 0
    for i in range(2,int(math.sqrt(a)+1)):
        if a%i == 0:
            f = 1
            return f
    return f
a = 1000
n = 3
m = 5
c = 0
for i in range(2,a): 
    if isprime(i)== 0:
        if c == n:
            n = i
        if c == m:
            m = i
            break
        c += 1
print(n,m)
print((n*m)-1)
