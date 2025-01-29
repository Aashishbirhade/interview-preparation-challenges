def char(a):
    r  = 0
    for i in a:
        r = r*26+(ord(i)-ord('A')+1)
    return r

a = "AA"
print(char(a))