a = [3, 1, 0, 4, 2, 3, 1]
li = []

for i in range(len(a)):
    if a[i] in a[i + 1:]:  # Check if a[i] exists in the remaining part of the list
        if a[i] not in li:  # Ensure the duplicate is added only once
            li.append(a[i])
li  = sorted(li)
print(li)
