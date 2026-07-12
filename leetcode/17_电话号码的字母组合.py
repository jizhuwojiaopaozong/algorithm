from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        d = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]

        def dfs(index, path):
            if index == len(digits):
                res.append(path)
                return
            for c in d[int(digits[index])]:
                dfs(index + 1, path + c)

        dfs(0, "")
        return res

solution = Solution()
print(solution.letterCombinations("23"))
print(solution.letterCombinations(""))
print(solution.letterCombinations("2"))
print(solution.letterCombinations("234"))
print(solution.letterCombinations("2345"))