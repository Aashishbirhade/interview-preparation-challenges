def istime(n):
    if n <= 2000:
        print("25 Minutes")
    elif n <= 4000:
        print("35 Minutes")
    elif n <= 7000:
        print("45 Minutes")
    else:
        print("Invalid")

n = int(input("enter weight of cloth "))
istime(n)