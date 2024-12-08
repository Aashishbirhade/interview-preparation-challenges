def occurance(a,t):
    c = 0
    for i in a:
        if i == t:
            c += 1
    return c

arr = [1,2,3,2,2,2]
t = 2
print(occurance(arr,t))

