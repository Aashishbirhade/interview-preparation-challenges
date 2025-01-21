def palindrome(a):
    for i in a:
        v = i
        rev = 0
        while i!=0:
            rem = i%10
            rev = rev*10 + rem
            i  //=10
        if v != rev:
            return False
    return True
a =[121,222,202]
print(palindrome(a))