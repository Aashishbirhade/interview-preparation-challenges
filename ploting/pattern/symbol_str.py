s = input("enter only * or #")
star = 0
hash = 0
for i in (s):
    if i !="*" and i !="#":
        print("invalid input")
        break
    else:
        if i == "*":
            star += 1
        else:
            hash += 1
print("heigher count is",star-hash)
