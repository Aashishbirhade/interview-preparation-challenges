a = 5
n = a*(a+1)//2
start = n
for i in range(a):
    val = start
    for j in range(i + 1):  # Fix here
        print(val, end="   ")
        val -= (j + 1)
    start -= (i + 1)
    print()
