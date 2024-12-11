a = [10, 20, 40, 30, 50, 20, 10, 20]
li = []
for i in range(len(a)):
    if a[i] in a[i+1:] and a[i] not in li:
        li.append(a[i])
print(li)