arr = [1, 2, 3, 7, 5]  
t = 12 
st = 0
end = 0
sumi = 0
result = (-1,)  

while st < len(arr) and end <= len(arr):
    if sumi == t:
        result = (st + 1, end)  
        break
    elif sumi > t:
        sumi -= arr[st]
        st += 1
    elif end < len(arr): 
        sumi += arr[end]
        end += 1
    else:  
        break


print(" ".join(map(str, result)))
