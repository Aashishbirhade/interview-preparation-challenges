def maxima(n,c,v):
    right = 0
    left = 0
    m = 0
    r = n-1
    for i in range(v):
        left += c[i]
    m = left
    for j in range(v-1,-1,-1):
        left -= c[j]
        right += c[r]
        r -= 1
        m = max(m,left+right)
    return m
        

n = 7
c = [1,2,3,4,5,6,1]
v = 3
print(maxima(n,c,v))

