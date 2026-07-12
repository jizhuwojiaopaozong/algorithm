from typing import List


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []
        path = []

        def dfs(start, n, k):
            if not n:
                if not k:
                    res.append(path[:])
                    return
            elif k:
                i = start
                while i <= 9:
                    if n >= i:
                        path.append(i)
                        dfs(i + 1, n - i, k - 1)
                        path.pop()
                    i += 1

        dfs(1, n, k)
        return res

solution = Solution()
print(solution.combinationSum3(3, 7))
print(solution.combinationSum3(3, 9))
print(solution.combinationSum3(4, 1))
print(solution.combinationSum3(4, 2))
print(solution.combinationSum3(4, 3))
print(solution.combinationSum3(4, 4))
print(solution.combinationSum3(4, 5))
print(solution.combinationSum3(4, 6))
print(solution.combinationSum3(4, 7))
print(solution.combinationSum3(4, 8))
print(solution.combinationSum3(4, 9))
print(solution.combinationSum3(4, 10))
