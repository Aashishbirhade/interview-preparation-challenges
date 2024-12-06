a,b = map(int,input().split())
sa = 0
for i in range(1,min(a,b)):
    if a%i==0 and b%i==0:
        sa = i
print(f"hcf of {a} and {b} is {sa}")