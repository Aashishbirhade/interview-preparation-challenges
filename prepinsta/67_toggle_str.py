a = "Aws"
v =" "
for i in a:
    if i.isupper():
        v += i.lower()
    elif i.islower():
        v += i.upper()
print(v)