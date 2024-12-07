# a = [2]
# for i in a:
#     if len(a) //2 < a.count(i):
#         print(i)
#         break
#     else:
#         print(-1)

def majorityElement(arr):
    
    candidate, count = None, 0
    for num in arr:
        if count == 0:
            candidate, count = num, 1
        elif num == candidate:
            count += 1
        else:
            count -= 1

    if arr.count(candidate) > len(arr) // 2:
        return candidate
    else:
        return -1
arr = [2,1,2,3,2]
print(majorityElement(arr))