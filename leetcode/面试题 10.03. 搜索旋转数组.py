from typing import List


# https://leetcode.cn/problems/search-rotate-array-lcci/description/
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        while r >= 0 and nums[r] == nums[0]:
            r -= 1
        while l < r:
            mid = (l + r + 1) // 2
            if nums[mid] >= nums[0]:
                l = mid
            else:
                r = mid - 1
        if target >= nums[0]:
            l = 0
        else:
            l = r + 1
            r = len(nums) - 1
        while l < r:
            mid = (l + r) // 2
            if nums[mid] >= target:
                r = mid
            else:
                l = mid + 1
        if nums[r] == target:
            return r
        else:
            return -1
