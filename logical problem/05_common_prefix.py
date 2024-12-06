arr = ["geeksforgeeks", "geeks", "geek", "geezer"]
pre = arr[0]
for i in (arr[1:]):
    temp = ""
    for j in range(min(len(pre),len(i))):
        if pre[j]==i[j]:
            temp += pre[j]
        else:
            break
    pre = temp

print(pre)