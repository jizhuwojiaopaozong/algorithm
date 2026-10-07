n, m = map(int, input().split())
volume = [0] * (n + 1)
value = [0] * (n + 1)
for i in range(1, n + 1):
    v1, v2 = map(int, input().split())
    volume[i] = v1
    value[i] = v2
f = [[0] * (m + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    for j in range(0, m + 1):
        f[i][j] = f[i - 1][j]
        if j >= volume[i]:
            f[i][j] = max(f[i][j], f[i - 1][j - volume[i]] + value[i])
print(f[n][m])
