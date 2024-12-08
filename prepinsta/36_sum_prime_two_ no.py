def prime(d):
    f = False
    for i in range(2,d):
        if d%i == 0:
            f = True
            return f
    return f
n = int(input("enter range element: "))
li =[]
for i in range(2,n):
    v = prime(i)
    if v==False:
        li.append(i)
print(li)
f = 0
for i in range(len(li)):
    for j in range(i+1,len(li)):
        if li[i] + li[j] == n:
            f = 1
            print(f"the given no {li[i]} + {li[j]} = {n}")
if f == 0:
    print("given no not have any prime exact sum")