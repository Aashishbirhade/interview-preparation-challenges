def medians(values, k):
    n = len(values)
    medians_list = []

    def generate(start, path):
        if len(path) == k:
            sorted_subseq = sorted(path)
            median_val = sorted_subseq[(k - 1) // 2]
            medians_list.append(median_val)
            return
        
     
        for i in range(start, n):
            generate(i + 1, path + [values[i]])

  
    generate(0, [])

    return [max(medians_list), min(medians_list)]


n = int(input().strip())
values = [int(input().strip()) for _ in range(n)]
k = int(input().strip())

result = medians(values, k)
print(result[0])  # max median
print(result[1])  # min median
