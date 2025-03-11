# def count(a):
#     c = 0
#     for i in n:
#         if a == i:
#             c += 1
#     return c 

# n = 'aabc'
# c = ''
# for i in (n):
#     v =  count(i)
#     c += i
#     c += str(v)
# print(c[::-1])


n = 'aaaabbcb'
a = ''
c = 1
for i in range(len(n)-1):
   
    if n[i] == n[i+1]:
        c += 1
    else:
        a += n[i] + str(c)
        c = 1
a += n[-1] + str(c)
print(a[::-1])


