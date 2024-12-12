arr =[1,-2,-3,0,7,-8,-2]
result = arr[0]

for i in range(len(arr)):
    
    mul = arr[i]
    
    # traversing in current subarray
    for j in range(i + 1, len(arr)):
        result = max(result, mul)
        mul *= arr[j]
        
    # updating the result for (n-1)th index.
    result = max(result, mul)
print(result)