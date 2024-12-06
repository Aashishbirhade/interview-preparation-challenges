# σ(6) / 6 = (1+2+3+6) / 6 = 2,
#  the same as σ(28) / 28 = (1+2+4+7+14+28) / 28 = 2.
#  The shared value 2 is an integer in this case but not in many other cases. Numbers with abundancy 2 are also known as perfect numbers.
a,b = map(int,input().split())
sa =0
sa1 = 0
for i in range(1,a+1):
    if a%i== 0:
        sa += i
for j in range(1,b+1):
    if b%j == 0:
        sa1 += j
print(sa,sa1)
if sa/a == sa1/b:
    print("friendly pair")
else:
    print("Not")

