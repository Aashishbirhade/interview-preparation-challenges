n = 5
a = [7,0,5,1,3] 
b = [1,2,1,3,4]
r = 0
ma = 0
for i in range(n):
    r =r +a[i] - b[i]
    ma = max(ma,r)
print(ma)  