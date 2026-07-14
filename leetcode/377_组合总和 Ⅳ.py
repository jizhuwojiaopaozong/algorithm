from typing import List


class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        f = [0] * (target + 1)
        f[0] = 1
        for i in range(1, target + 1):
            for num in nums:
                if i >= num:
                    f[i] += f[i - num]
        return f[target]

solution = Solution()
print(solution.combinationSum4([1, 2, 3], 4))
print(solution.combinationSum4([9], 3))
print(solution.combinationSum4([1, 2, 3], 5))
print(solution.combinationSum4([1, 2, 3], 6))
print(solution.combinationSum4([1, 2, 3], 7))
print(solution.combinationSum4([1, 2, 3], 8))
print(solution.combinationSum4([1, 2, 3], 9))
print(solution.combinationSum4([1, 2, 3], 10))