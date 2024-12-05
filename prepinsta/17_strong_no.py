n = int(input())
a =n
sumi = 0
while n != 0:
    rem = n % 10
    fact = 1
    for i in range(1, rem+1):
        fact *= i
    sumi += fact 
    n //= 10
if sumi == a:
    print("given no is strong no")
else:
    print("Given no is not strong")
