from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        if nums[l] <= nums[r]:
            return nums[0]
        while l < r:
            mid = (l + r) // 2
            if nums[mid] >= nums[0]:
                l = mid + 1
            else:
                r = mid
        return nums[r]


solution = Solution()
print(solution.findMin([3,4,5,1,2]))
print(solution.findMin([4,5,6,7,0,1,2]))
print(solution.findMin([11,13,15,17]))