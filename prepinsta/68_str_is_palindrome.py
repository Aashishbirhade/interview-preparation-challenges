def is_palidrome(a):
    i = 0
    j = len(a)-1
    while i<=j:
        if a[i] != a[j]:
            return False
        i +=1
        j -= 1
    return True
a = input("Enter any Str ")
if is_palidrome(a):
    print("Given Str is Palindrome")
else:
    print("NOT")