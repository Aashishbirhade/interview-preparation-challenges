a = int(input())
b = a
rev = 0
while a!=0:
    rem = a%10
    rev = rem + rev*10
    a//=10

if rev==b:
    print("Give No is Palindrom")
else:
    print("not ")
