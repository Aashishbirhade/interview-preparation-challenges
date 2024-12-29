a = {'india':1,'eng':2,'Uk':3}
v = "pl"
c = list(a.items())
for i in range (len(c)):
    if c[i][0] == v:
        print(f"value is {c[i]}")
