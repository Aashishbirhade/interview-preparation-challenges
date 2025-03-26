n = 5
v = 10
for i in range(1,n):
    for j in range(n-i):
        print(" ",end=" ")
    st = v
    for j in range(n):
        if i%2==0:
            print(st+n-1-j ,end=" ")#v+n-j-1
        else:
            print(v ,end=" ")
        v += 1
    print(" ")


#         10 11 12 13 14  
#       19 18 17 16 15
#     20 21 22 23 24
#   29 28 27 26 25