a = "1A3"
i = len(a)-1
s = 0
c = 0
while i>=0:
    if a[i] >= '0' and a[i] <= '9':
        v = int(a[i])
    elif a[i] >= 'A' and a[i] <='F':
        v = ord(a[i]) - 55
    s += v*(16**c) 
    c += 1
    i -= 1
print(s)