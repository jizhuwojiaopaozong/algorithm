class Solution:
    def maxProfit(self, k, prices):
        n = len(prices)
        if k >= n // 2:
            res = 0
            i = 0
            while i < n - 1:
                if prices[i + 1] > prices[i]:
                    res += prices[i + 1] - prices[i]
                i += 1
            return res

        f = [[float("-inf")] * (k + 1) for _ in range(n + 1)]
        g = [[float("-inf")] * (k + 1) for _ in range(n + 1)]
        f[0][0] = 0
        res = 0
        for i in range(1, n + 1):
            for j in range(0, k + 1):
                f[i][j] = max(f[i - 1][j], g[i - 1][j] + prices[i - 1])
                g[i][j] = g[i - 1][j]
                if j:
                    g[i][j] = max(g[i][j], f[i - 1][j - 1] - prices[i - 1])
                res = max(res, f[i][j])
        return res


print(Solution().maxProfit(2, [2, 4, 1]))
# print(Solution().maxProfit(2, [3, 2, 6, 5, 0, 3]))
