a = [10, 20, 40, 30, 50, 20, 10, 20]
li = []
for i in a:
    if i not in li:
        li.append(i)
print(len(li))