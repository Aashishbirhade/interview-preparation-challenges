def find_leaders(arr):
    n = len(arr)
    leaders = []
    max_from_right = float('-inf')
 
    for i in range(n - 1, -1, -1):
        if arr[i] >= max_from_right:
            leaders.append(arr[i])  
            max_from_right = arr[i]  
    
    leaders.reverse()
    return leaders


print(find_leaders([16, 17, 4, 3, 5, 2]))
print(find_leaders([10, 4, 2, 4, 1]))      
print(find_leaders([5, 10, 20, 40]))       
print(find_leaders([30, 10, 10, 5]))      
