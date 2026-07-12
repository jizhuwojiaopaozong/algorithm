from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]):

        def reverse(start, end):
            while start < end:
                tmp = nums[start]
                nums[start] = nums[end]
                nums[end] = tmp
                start += 1
                end -= 1

        i = len(nums) - 1
        while i and nums[i - 1] >= nums[i]:
            i -= 1
        if i <= 0:
            reverse(0, len(nums) - 1)
        else:
            j = i
            while j < len(nums) and nums[j] > nums[i - 1]:
                j += 1
            tmp = nums[j - 1]
            nums[j - 1] = nums[i - 1]
            nums[i - 1] = tmp
            reverse(i, len(nums) - 1)
        return nums

solution = Solution()
print(solution.nextPermutation([1, 2, 3]))
print(solution.nextPermutation([3, 2, 1]))
print(solution.nextPermutation([1, 1, 5]))
print(solution.nextPermutation([1, 3, 2]))
print(solution.nextPermutation([2, 3, 1]))
print(solution.nextPermutation([3, 1, 2]))
print(solution.nextPermutation([2, 1, 3]))
print(solution.nextPermutation([1, 2, 3]))
print(solution.nextPermutation([3, 2, 1]))