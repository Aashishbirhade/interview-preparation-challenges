a = [12, 3, 4, 22, 5, 7, 65]
k = 2
for i in range(k):
    mini = a[0]
    for j in a:
        if mini >= j:
            mini = j
    a.remove(mini)
print(mini)