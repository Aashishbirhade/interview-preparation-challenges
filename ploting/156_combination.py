def combination(a):
    fact = 1
    for i in range(1,a+1):
        fact *= i
    return fact
n = 5
r = 0
if r > n:
    print(0)
else:
    u = combination(n)
    l = combination(r)*(combination(n-r))
    print(u//l)