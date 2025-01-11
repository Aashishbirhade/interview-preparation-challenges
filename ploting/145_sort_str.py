b = 'bbcsdatuor'
a = list(b)
for i in range(len(a)):
    for j in range(len(a)-i-1):
        if a[j] > a[j+1]:
            a[j],a[j+1] = a[j+1],a[j]
print("".join(a))
print("".join(sorted(b)))