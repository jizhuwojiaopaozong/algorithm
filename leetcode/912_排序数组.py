import random

class Solution:
    def quick_sort(self, l, r):
        if l >= r:
            return
        i = l - 1
        j = r + 1
        x = self.nums[random.randint(l, r)]
        while i < j:
            i += 1
            while self.nums[i] < x:
                i += 1
            j -= 1
            while self.nums[j] > x:
                j -= 1
            if i < j:
                tmp = self.nums[i]
                self.nums[i] = self.nums[j]
                self.nums[j] = tmp
        self.quick_sort(l, j)
        self.quick_sort(j + 1, r)

    def sortArray(self, nums: List[int]) -> List[int]:
        self.nums = nums
        self.quick_sort(0, len(nums) - 1)
        return self.nums
        