arr = [15, -2, 2, -8, 1, 7, 10, 23]
s = 0 
max_len = 0  
indices = [] 
for i in range(len(arr)):
    s += arr[i]
    if s == 0:
        max_len = i + 1 

    if s in indices:
        first_index = indices.index(s)  
        max_len = max(max_len, i - first_index) 
    else:
        indices.append(s)  
print(max_len) 
