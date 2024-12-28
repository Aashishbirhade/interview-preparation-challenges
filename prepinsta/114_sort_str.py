a = "geekforgeeks"
# v = "".join(sorted(a))
# print(v)
a = list(a)
for i in range(len(a)):
    for j in range(len(a)-i-1):
        if a[j] < a[j+1]:
            a[j],a[j+1] = a[j+1],a[j]
print("".join(a))
