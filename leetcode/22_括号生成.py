from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def dfs(l, r, path):
            if l == n and r == n:
                res.append(path)
            else:
                if l < n:
                    dfs(l + 1, r, path + "(")
                if r < n and l > r:
                    dfs(l, r + 1, path + ")")

        dfs(0, 0, "")
        return res


sol = Solution()
print(sol.generateParenthesis(3))
print(sol.generateParenthesis(1))
