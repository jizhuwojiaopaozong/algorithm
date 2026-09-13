from typing import List


class Solution:
    def climbStairs(self, n: int) -> int:
        a = 1
        b = 1
        for i in range(n):
            c = a + b
            a = b
            b = c
        return a

    # 扩展约束：不能踩到第 7 步以及 7 的倍数步（7, 14, 21, 28...）。
    def climbStairs1(self, n: int) -> int:
        a = 1
        b = 1
        for i in range(2, n + 1):
            if i % 7 == 0:
                a = b
                b = 0
            else:
                c = a + b
                a = b
                b = c
        return b

    # 输出"具体路径"，回溯/dfs
    def climbStairs2(self, n: int) -> List[int]:
        res = []

        def dfs(step, path):
            if step == n:
                res.append(path[:])
                return
            for i in range(1, 3):
                cur = step + i
                # if cur <= n and cur % 7 != 0:
                if cur <= n:
                    path.append(cur)
                    dfs(cur, path)
                    path.pop(-1)

        dfs(0, [0])
        return res

    # 输出"具体路径"，回溯/dfs，并且不能连续跳两次 1 格
    def climbStairs3(self, n: int) -> List[int]:
        res = []

        def dfs(step, path, last_step):
            if step == n:
                res.append(path[:])
                return
            for i in range(1, 3):
                if i == 1 and last_step == 1:
                    continue
                cur = step + i
                if cur <= n:
                    path.append(cur)
                    dfs(cur, path, i)
                    path.pop()

        dfs(0, [0], 0)
        return res

    def climbStairs4(self, n: int) -> int:
        if n == 0:
            return 1
        f = [[0, 0] for _ in range(n + 1)]
        # f[i][0] 表示达到第i步，且最后一步是跳1步上来的方案数
        # f[i][1] 表示达到第i步，且最后一步是跳2步上来的方案数
        f[1][0] = 1
        f[2][1] = 1
        for i in range(3, n + 1):
            f[i][0] = f[i - 1][1]
            f[i][1] = f[i - 2][0] + f[i - 2][1]
        return f[n][0] + f[n][1]

    # 每次最多爬m阶台阶时的方案数（每次可爬1，2，3，4，...m）
    def climbStairs5(self, n: int, m: int) -> int:
        f = [0] * (n + 1)
        f[0] = 1
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if i >= j:
                    f[i] += f[i - j]
        return f[n]


solution = Solution()
# print(solution.climbStairs(2))
# print(solution.climbStairs(3))
# print(solution.climbStairs1(2))
# print(solution.climbStairs1(3))
# print(solution.climbStairs1(7))
# print(solution.climbStairs1(8))

# print(solution.climbStairs2(2))
# print(solution.climbStairs2(3))
# print(solution.climbStairs2(7))
# print(solution.climbStairs2(8))
# print(solution.climbStairs3(8))
# print(solution.climbStairs4(8))

print(solution.climbStairs5(5, 2))
print(solution.climbStairs5(5, 3))
print(solution.climbStairs5(5, 4))
print(solution.climbStairs5(5, 5))
