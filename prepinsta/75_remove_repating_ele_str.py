def is_repeted(i):
    c = 0
    for j in a:
        if i== j:
            c += 1
    return c
a ='prepinsta'
for i in a:
    v = is_repeted(i)
    if v == 1:
        print(i,end = " ")