a = 12 
b = 14
lcm = 0 #common multiple 84
for i in range(max(a,b),1+(a*b)):
   if i%a==0 and i%b == 0:
    lcm = i
    break


print(lcm)