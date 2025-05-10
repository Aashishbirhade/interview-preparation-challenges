n = 9
arr = [4,5,0,1,9,0,5,0]
r  = []
c = 0
for i in range(len(arr)):
    if arr[i] != 0:
        r.append(arr[i])
    else:
        c += 1
for i in range(c):
    r.append(0)

print(r)