a = 1212
rev = 0
while a!=0:
   rem =  a% 10
   rev = rem + rev*10
   a//= 10
print(rev)