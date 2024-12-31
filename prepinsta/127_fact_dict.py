def fact(i):
    fact = 1
    for j in range(1,i+1):
        fact *= j
    return fact
a = {"a":10,"b":2,"c":5,"x":4,"e":6}
x = {}
for i,j in a.items():
    v = fact(j)
    x[i] = v
print("before dict : ",a)
print("after fact dict : ",x)
