a = 1020
m =1
result = 0
while a!=0:
    rem = a%10
    if rem == 0:
        rem = 5
    result = rem*m +result
    m *= 10
    a //=10
print(result)