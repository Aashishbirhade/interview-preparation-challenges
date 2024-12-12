p= [(3, 4), (1, 2), (5, 2), (7, 10), (4,3), (2, 5)]
# for i,(a,b) in enumerate(p):
#     for j,(c,d) in enumerate(p):
#         if i <j and (a == d and b==c):
#             print((a,b),end =" ")
s = set()
for (a,b) in p:
    s.add((a,b))
    if (b,a) in s:
        print((a,b),end = " ")
