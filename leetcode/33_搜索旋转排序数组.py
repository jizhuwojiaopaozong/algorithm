from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 0:
            return -1
        l = 0
        r = len(nums) - 1
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


s = Solution()
# print(s.search([4,5,6,7,0,1,2], 0))
# print(s.search([4,5,6,7,0,1,2], 3))
print(s.search([1], 0))