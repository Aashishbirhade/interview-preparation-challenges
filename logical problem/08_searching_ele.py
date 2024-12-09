def search(k, arr):
        
        for i in range(len(arr)):
            if arr[i] == k:
                return i+1
        return -1


a =  [1, 2, 3, 4, 5, 5] 
k = 5
print(search(k,a))

        
    