a = [1 ,2, 0, 2, 1, 0, 2, 1, 0, 2, 0, 1]
count_0 = a.count(0)
count_1 = a.count(1)
count_2 = a.count(2)
new_arr = []
for i in range(count_0):
    new_arr.append(0)
for i in range(count_1):
    new_arr.append(1)
for i in range(count_2):
    new_arr.append(2)
print(" After sorting:", new_arr)


