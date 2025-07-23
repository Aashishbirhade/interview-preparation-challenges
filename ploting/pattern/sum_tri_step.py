# a = 5
# n = a*(a+1)//2
# start = n
# for i in range(a):
#     val = start
#     for j in range(i + 1):  # Fix here
#         print(val, end="   ")
#         val -= (a-(i-j))
#     start -= 1
#     print()



a = 5
n = a*(a+1)//2
start = n
for i in range(a):
    val = start
    for j in range(i + 1):
        print(val, end="   ")
        val -= (a - j - 1)  # This is the key change
    start -= 1
    print()