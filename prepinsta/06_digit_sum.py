n = int(input())
sumi = 0

while n != 0:
    rem = n % 10
    sumi += rem
    n //= 10

print(sumi)
