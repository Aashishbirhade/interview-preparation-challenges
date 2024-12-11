
def frequency(i):
    c = 0
    for j in a:
        if i==j:
            c+=1
    return c

a = [10, 20, 70, 90, 80, 20, 10, 20]

for i in (a):
    cou = frequency(i)
    if cou==1:
        print(i,end=" ")

