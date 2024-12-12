a = [11,21,33,44,67]
b =[11,33,1,44]
f = False
for i in range(len(b)):
    if b[i] not in a:
        f = True
if f == False:
    print("B is subset of a")
