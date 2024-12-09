dig = '121'
a = len(dig)
cnt = [0] * (a + 1)
cnt[0], cnt[1] = 1, 1

for k in range(2, a + 1):
    cnt[k] = 0
    cnt[k] = cnt[k - 1]

    if dig[k - 2] == '1' or (dig[k - 2] == '2' and dig[k - 1] < '7'):
        cnt[k] += cnt[k - 2]

print(cnt[a])



