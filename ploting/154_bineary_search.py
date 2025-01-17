def bineary_search(a,n,key):
    st = 0
    end = n
    while st <= end:
        mid = (st+ end)// 2
        if a[mid] == key:
            return mid 
            
        elif a[mid] > key:
            end = mid - 1
        elif a[mid] < key:
            st = mid + 1
    return -1



a =[2,4,5,6,7,8,9,10,14]
key = 14
print(bineary_search(a,len(a)-1,key))