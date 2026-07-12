from typing import List


class Solution:
    def maxProfit(self, nums: List[int]) -> int:
        res = 0
        i = 0
        while i < len(nums) - 1:
            res += max(0, nums[i + 1] - nums[i])
            i += 1
        return res

solution = Solution()
print(solution.maxProfit([7, 1, 5, 3, 6, 4]))
print(solution.maxProfit([1, 2, 3, 4, 5]))
print(solution.maxProfit([7, 6, 4, 3, 1]))
print(solution.maxProfit([1, 2, 3, 4, 5]))
print(solution.maxProfit([1, 2, 3, 4, 5]))