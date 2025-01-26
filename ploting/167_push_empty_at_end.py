a = [2,0,1,2,1,0]
r = []
c = 0
for i in a:
    if i ==0:
        c +=1
    else:
        r.append(i)
for i in range(c):
    r.append(0)
print(r)