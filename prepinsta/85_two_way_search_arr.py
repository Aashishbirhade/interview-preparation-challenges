a = [-1, 0, 1, 3, 3, 4, 9, 10]
t = 3
st = 0
end = len(a) - 1

while st <= end:
    if a[st] != t:  
        st += 1
    elif a[end] != t: 
        end -= 1
    else:  
        print(a[st], a[end])
        break
