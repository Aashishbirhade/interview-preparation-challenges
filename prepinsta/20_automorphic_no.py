a = 75
b = len(str(a))
#out 625
sq = str(a**2)
z = sq[-b:]
if int(z) == a:
    print("given no is Automorphic")
else:
    print("NOT")
