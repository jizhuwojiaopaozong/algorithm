from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        if nums[l] < nums[r]:
            return nums[l]
        while r >= 0 and nums[r] == nums[l]:
            r -= 1
        if r < 0:
            return nums[l]
        if nums[r] > nums[l]:
            return nums[l]
        while l < r:
            mid = (l + r) // 2
            if nums[mid] >= nums[0]:
                l = mid + 1
            else:
                r = mid
        return nums[r]

solution = Solution()
print(solution.findMin([1, 3, 5]))
print(solution.findMin([2, 2, 2, 0, 1, 2]))
print(solution.findMin([1, 2, 1]))

