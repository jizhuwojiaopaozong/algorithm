from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        if len(nums) == 0:
            return False
        r = len(nums) - 1
        while r >= 0 and nums[r] == nums[0]:
            r -= 1
        if r < 0:
            return nums[0] == target
        l = 0
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
            return True
        else:
            return False


solution = Solution()
print(solution.search([2,5,6,0,0,1,2], 0))
print(solution.search([2,5,6,0,0,1,2], 3))