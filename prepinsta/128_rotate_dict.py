a = {"a":10,"b":2,"c":5,"x":4,"e":6}
v = list(a.items())
r = v[-1:]+v[:-1]
print(dict(r))