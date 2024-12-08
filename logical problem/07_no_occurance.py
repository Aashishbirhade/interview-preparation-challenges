def occurance(a,t):
    c = 0
    for i in a:
        if i == t:
            c += 1
    return c

arr = [1,2,3,2,2,2]
t = 2
print(occurance(arr,t))

# arr = [100000, 100000, 100000]
# n = 1
# for i in arr:
#     n *= i
# print(n% 1000000007)
            