a = "aa123bcw"
c = ""
n = ""
for i in a:
    if i.isalpha():
        c += i
    else:
        n += i
print([c,n])