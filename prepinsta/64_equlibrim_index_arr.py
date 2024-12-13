a =  [-4, 1, 5, 2, -4, 4, 2]
mid = len(a)//2
sl = 0
sr = 0
for i in range(mid):
    sl += a[i]

for i in range(mid+1,len(a)):
    sr += a[i]

if sl == sr:
    print("equlibirim index is ",mid)
else:
    print("NOT")
