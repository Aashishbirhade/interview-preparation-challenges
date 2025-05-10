import math
a = 10
k =(1<<int(math.log2(a)+1)-1)
print(a^k,k)


# Let’s say a = 10 → binary: 1010 (4 bits)
# math.log2(10) ≈ 3.32
# math.log2(10) + 1 ≈ 4.32
# int(...) = 4
# 1 << 4 = 16   a << n = 2^n  1000
# 1 << 1 = 2     # 0001 => 0010
# 1 << 2 = 4     # 0001 => 0100
# 1 << 3 = 8     # 0001 => 1000
# 16 - 1 = 15 → binary: 1111