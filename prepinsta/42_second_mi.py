arr = [3,5,1,9,7]
mi1 = arr[0]
mi2 = arr[0]
for i in (arr):
    if mi1 > i:
        mi1 = i
for i in arr:
    if mi1 >i and i > mi2:
        mi2 = i
print(f" first :{mi1} second :{mi2}")