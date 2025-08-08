a = 3
s = [2,3,1]
total = 0 
for i in range(len(s)):
    curr_min = s[i]
    curr_max = s[i]
    for j in range(i,len(s)):
        curr_min = min(curr_min,s[j])
        curr_max = max(curr_max,s[j])
        total += (curr_max-curr_min)
print(total)