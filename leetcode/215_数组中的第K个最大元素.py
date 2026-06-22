class Solution:
    def quick_sort(self, l, r, k):
        if l == r:
            return self.nums[k]
        i = l - 1
        j = r + 1
        tar = self.nums[l]
        while i < j:
            i += 1
            while self.nums[i] > tar:
                i += 1
            j -= 1
            while self.nums[j] < tar:
                j -= 1
            if i < j:
                tmp = self.nums[i]
                self.nums[i] = self.nums[j]
                self.nums[j] = tmp
        if k <= j:
            return self.quick_sort(l, j, k)
        else:
            return self.quick_sort(j + 1, r, k)

    def findKthLargest(self, nums, k) -> int:
        self.nums = nums
        return self.quick_sort(0, len(nums) - 1, k - 1)

solution = Solution()
# print(solution.findKthLargest([3,2,1,5,6,4], 2))
print(solution.findKthLargest([3,2,3,1,2,4,5,5,6], 4))