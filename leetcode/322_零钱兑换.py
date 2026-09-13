from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        f = [[float("inf")] * (amount + 1) for _ in range(len(coins) + 1)]
        f[0][0] = 0
        for i in range(1, len(coins) + 1):
            for j in range(0, amount + 1):
                f[i][j] = f[i - 1][j]
                if j >= coins[i - 1]:
                    f[i][j] = min(f[i][j], f[i][j - coins[i - 1]] + 1)
        if f[len(coins)][amount] == float("inf"):
            return -1
        else:
            return f[len(coins)][amount]


solution = Solution()
print(solution.coinChange([1, 2, 5], 11))
print(solution.coinChange([2], 3))
print(solution.coinChange([1], 0))
