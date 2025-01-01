a = {"a":10,"b":2,"c":5,"x":4,"e":6}
n = 3
ma = 0
ma_ki = None
for i in range(n):
    ma = 0
    ma_ki = None
    for j,k in (a.items()):
       if ma < k:
        ma = k
        ma_ki = j
    a.pop(ma_ki)
print(ma)