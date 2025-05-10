import math
a = 10
k =(1<<int(math.log2(a)+1)-1)
print(a^k,k)
