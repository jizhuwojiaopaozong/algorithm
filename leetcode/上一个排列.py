from typing import List


class Solution:
    def prevPermutation(self, nums: List[int]) -> None:
        i = len(nums) - 1
        while i and nums[i - 1] <= nums[i]:
            i -= 1
        if i == 0:
            nums.reverse()
            return
        else:
            j = i
            while j < len(nums) and nums[j] < nums[i - 1]:
                j += 1
            nums[i - 1], nums[j - 1] = nums[j - 1], nums[i - 1]
            nums[i:] = nums[i:][::-1]
            return


sol = Solution()
nums = [3, 2, 1]
print(nums)
sol.prevPermutation(nums)
print(nums)
