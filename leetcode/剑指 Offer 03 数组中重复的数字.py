from typing import List


class Solution:
    def findRepeatNumber(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            while i != nums[i]:
                if nums[i] == nums[nums[i]]:
                    return nums[i]
                else:
                    nums[nums[i]], nums[i] = nums[i], nums[nums[i]]
        return -1


s = Solution()
print(s.findRepeatNumber([2, 3, 1, 0, 2, 5, 3]))
