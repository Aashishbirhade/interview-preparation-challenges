a = int(input("Enter any decimal NO. :"))
s = ""
while a!=0:
    if a%2==0:
        s = '0'+ s
    else:
        s= '1' +s
        
    a //= 2
print(s)
