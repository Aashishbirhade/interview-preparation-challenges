a = [1,57,35,20,8,43,90,2,98,3,7]
n = len(a)
a.sort()
li = []
mid = n // 2
for i in range(mid):
    li.append(a[i])
for i in range(n - 1, mid-1, -1):
    li.append(a[i])
print("Half Ascending and Half Descending:", li)