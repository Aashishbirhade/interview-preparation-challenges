def frequency(i):
    c = 0 
    for j in a:
        if i == j:
            c += 1
    return c

a = [3, 1, 2, 2, 3, 3, 4, 4, 4, 4]
n = 4 
d = set()
for i in a:
    v = frequency(i)
    if v > len(a)/n:
        d.add(i)
print(d)

        
