a = [10,20,30,30,20,10,40]
li = []
for i in a:
    if i not in li:
        li.append(i)
print(li)