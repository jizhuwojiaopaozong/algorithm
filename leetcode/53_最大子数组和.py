class Solution:
    def maxSubArray(self, nums):
        res = -(2**31)
        last = 0
        for i in range(len(nums)):
            last = nums[i] + max(0, last)
            res = max(res, last)
        return res

    def maxSubArray_2(self, nums):
        res = -(2**31)
        last = 0
        tmp = -1
        for i in range(len(nums)):
            last = nums[i] + max(0, last)
            if last > res:
                res = last
                tmp = i
        ans = []
        while tmp >= 0:
            ans.append(nums[tmp])
            if res - sum(ans) == 0:
                break
            tmp -= 1
        ans.reverse()
        return ans


solution = Solution()
# print(solution.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
# print(solution.maxSubArray([5,4,-1,7,8]))
# print(solution.maxSubArray_2([-2,1,-3,4,-1,2,1,-5,4]))
# print(solution.maxSubArray_2([1]))
print(solution.maxSubArray_2([5, 4, -1, 7, 8]))
