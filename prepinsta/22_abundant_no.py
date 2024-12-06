a = 12
sa = 0
for i in range(1,a):
    if a%i== 0:
       sa += i
if sa>a:
    print("given no is abudant")
else:
    print("Not")