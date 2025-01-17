def marge(a,st,mid,end):
    li =[]
    left = st
    right = mid+1
    while left <=mid and right<=end:
        if a[left] <=a[right]:
            li.append(a[left])
            left += 1
        else:
            li.append(a[right])
            right += 1
    while left <= mid:
        li.append(a[left])
        left+=1
    while right <= end:
        li.append(a[right])
        right += 1
    for i in range(len(li)):
        a[st+i] = li[i]
def marge_func(a,st,end):
    if st<end:
        mid = (st+end)//2
        marge_func(a,st,mid)
        marge_func(a,mid+1,end)
        marge(a,st,mid,end)


a =[10,2,30,4,54,5,62,43,8,55]
marge_func(a,0,len(a)-1)
print(a)