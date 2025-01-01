a = {"a":10,"b":2,"c":5,"x":4,"e":6}
n = 3
mini = float('inf')
mi_ki = None
for i in range(n):
    mini = float('inf')
    mi_ki = None
    for j,k in (a.items()):
       if mini > k:
        mini = k
        mi_ki = j
    a.pop(mi_ki)
print(mini)