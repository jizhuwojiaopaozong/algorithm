from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        path = []
        candidates.sort()

        def dfs(index, target):
            if not target:
                res.append(path[:])
                return
            if index == len(candidates):
                return

            k = index + 1
            while k < len(candidates) and candidates[k] == candidates[index]:
                k += 1
            cnt = k - index

            i = 0
            while candidates[index] * i <= target and i <= cnt:
                dfs(k, target - candidates[index] * i)
                path.append(candidates[index])
                i += 1

            i = 0
            while candidates[index] * i <= target and i <= cnt:
                path.pop()
                i += 1

        dfs(0, target)
        return res

solution = Solution()
print(solution.combinationSum2([10, 1, 2, 7, 6, 1, 5], 8))
print(solution.combinationSum2([2, 5, 2, 1, 2], 5))
print(solution.combinationSum2([1], 1))
print(solution.combinationSum2([1], 2))
print(solution.combinationSum2([1], 3))
print(solution.combinationSum2([1], 4))
print(solution.combinationSum2([1], 5))
print(solution.combinationSum2([1], 6))
print(solution.combinationSum2([1], 7))