def isoccurance(li, a):
    dict ={}
    for i in li:
        if i in dict:
            dict[i] += 1
        else:
            dict[i] = 1
    return dict
a =5
li = [2,2,3,4,4]
dict = isoccurance(li, a)
for i,j in dict.items():
    if j%2 != 0:
        print(i)
        break