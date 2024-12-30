a = {"a":100,"b":21,"c":33,"x":11,"e":21}
ma_key, ma = next(iter(a.items()))
mi_key, mi = ma_key, ma
print(next(iter(a.items())))
for i,j in a.items():
    if ma < j:
        ma = j 
        ma_key = i
    if mi > j:
        mi = j
        mi_key = i
print(f"{ma_key}:{ma}")
print(f"{mi_key}:{mi}")