a = 28
li=[]
for i in range(1,a):
    if a%i==0:
        li.append(i)
print(li,sum(li))
if sum(li)== a:
    print("Given no is perfect ")
else:
    print("NOT")
