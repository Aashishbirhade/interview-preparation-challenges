def ispalindrome(a):
    rev  = 0
    b = a
    while a!=0:
        rem = a%10
        rev = rem +rev*10
        a //= 10
    if rev == b:
        return True
    else:
        return False


li = []
a = [133,2002,231,303]
for i in a:
    v = ispalindrome(i)
    if v == True:
        li.append(i)
print(max(li))