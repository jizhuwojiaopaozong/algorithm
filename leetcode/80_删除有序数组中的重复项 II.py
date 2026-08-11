from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 0
        for c in nums:
            if k < 2 or (c != nums[k - 1] or c != nums[k - 2]):
                nums[k] = c
                k += 1
        return k


sol = Solution()
print(sol.removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))
print(sol.removeDuplicates([1, 1, 1, 2, 2, 3]))
print(sol.removeDuplicates([0, 0, 1, 1, 1, 1, 2, 3, 3]))
