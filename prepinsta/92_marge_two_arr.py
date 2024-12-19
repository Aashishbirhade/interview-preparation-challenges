a = [1,2,3,5,6,7]
b = [4,8,9]
li = []
i = 0
j = 0
while i < len(a) and j < len(b):
    if a[i] <= b[j]:
        li.append(a[i])
        i += 1
    else:
        li.append(b[j])
        j += 1 
while i <len(a):
    li.append(a[i])
    i+= 1
while j <len(b):
    li.append(b[j])
    j+= 1
print(li)