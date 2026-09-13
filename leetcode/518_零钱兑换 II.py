from typing import List


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        f = [0] * (amount + 1)
        f[0] = 1
        for i in range(1, len(coins) + 1):
            for j in range(0, amount + 1):
                if j >= coins[i - 1]:
                    f[j] += f[j - coins[i - 1]]
        return f[amount]

    # 输出所有的组合，递归/回溯
    # 回溯求排列：每次从头选（for i in range(len)）。
    # 回溯求组合：按序向后选（for i in range(start_index, len)）。
    def change1(self, amount: int, coins: List[int]) -> List[List[int]]:
        res = []

        def dfs(n, path, start_index):
            if n == amount:
                res.append(path[:])
                return
            for i in range(start_index, len(coins)):
                if n + coins[i] <= amount:
                    path.append(coins[i])
                    dfs(n + coins[i], path, i)
                    path.pop()

        dfs(0, [], 0)
        return res


solution = Solution()
print(solution.change(5, [1, 2, 5]))
print(solution.change1(5, [1, 2, 5]))
print(solution.change(3, [2]))
print(solution.change1(3, [2]))
print(solution.change(10, [10]))
print(solution.change1(10, [10]))
print(solution.change1(0, [10]))
