arr = [100, 2, 70, 12 , 90]
s = sorted(arr) #2,12,70,90,100
print(s)
for i in range(len(arr)):
    for j in range(len(s)):
        if arr[i] == s[j]:
            print(j+1,end=" ")
