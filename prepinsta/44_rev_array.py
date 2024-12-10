a = [1,2,3,510,31]
st = 0
end = len(a)-1
while st<= end:
    tem = a[st]
    a[st] = a[end]
    a[end] = tem
    st +=1
    end -= 1
print(a)
    