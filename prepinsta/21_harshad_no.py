n = 21
sa = 0
while n != 0:
    rem = n % 10
    sa += rem
    n //= 10

if n % sa == 0:
    print("Given No. is Harshada")
else:
    print("It is not")
