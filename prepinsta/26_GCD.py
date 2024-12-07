#common divible value
a = 36
b = 60
GDC =0
for i in range(2,min(a,b)):
    if a%i == b%i==0:
        GDC = i
print(GDC)