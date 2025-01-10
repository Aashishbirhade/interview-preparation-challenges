def permutation(s,a,n):
    if a == n:
        print("".join(s))
    else:
         for i in range(a, n+1):
            s[a], s[i] = s[i], s[a]  
            permutation(s, a + 1, n)  
            s[a], s[i] = s[i], s[a] 
a = "ABC"
s = list(a)
permutation(s,0,len(a)-1)