a = ['eat', 'ate', 'cat', 'tae', 'tca', 'dog']
v = []

for i in a:
    c = sorted(i) 
    t = False

    for j in v:
        if sorted(j[0]) == c:  
            j.append(i)  
            t = True
            break

    if not t:
        v.append([i])  

print(v)
