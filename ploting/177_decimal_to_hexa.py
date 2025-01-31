n = 26
if n <= 9:
    print(n)
else:
    s = ""
    while n!=0:
        rem = n % 16
        if n > 9:
            g = chr(55+rem)
        else:
            g = str(rem)
        s = g + s
        n //= 16
print(s)