def frequency(i):
    c = 0
    for j in a:
        if i==j:
            c+=1
    return c
a =[2,3,5,5,5,4,1,2,5,4,3]
li =[]
for i in (a):
    cou = frequency(i)
    if cou >=2:
        li.append(i)
li.sort(reverse=True)
for i in range(len(a)):
    if a[i] in li:
        continue
    else:
        li.append(a[i])
print(li)