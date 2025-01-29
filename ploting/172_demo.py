a = "hi my self aashish"
b = "hi my self veer"
a = a.split()
b = b.split()
print(set(a).symmetric_difference(set(b)))