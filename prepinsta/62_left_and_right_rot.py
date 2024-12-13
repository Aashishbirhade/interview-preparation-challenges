def first_to_last(a):
    for i in range(len(a)-1):
        a[i],a[i+1] = a[i+1],a[i]
    return(a)
def last_to_first(a):    
    for j in range(len(a)-1,0,-1):
        a[j],a[j-1] = a[j-1],a[j]
    return (a)
a = [1,2,3,4,5]
b = list(a)
print(first_to_last(a))
print(last_to_first(b))

