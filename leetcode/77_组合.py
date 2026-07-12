class Solution:
    def combine(self, n, k):
        res = []
        path = []

        def dfs(n, k, start):
            if not k:
                res.append(path[:])
                return
            for i in range(start, n + 1):
                path.append(i)
                dfs(n, k - 1, i + 1)
                path.pop()

        dfs(n, k, 1)
        return res

solution = Solution()
print(solution.combine(4, 2))
print(solution.combine(1, 1))
print(solution.combine(5, 3))
print(solution.combine(5, 4))
print(solution.combine(5, 5))
print(solution.combine(5, 6))
print(solution.combine(5, 7))
print(solution.combine(5, 8))
print(solution.combine(5, 9))