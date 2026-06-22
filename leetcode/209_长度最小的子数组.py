class Solution:
    def minSubArrayLen(self, target, nums):
        res = 2**31 - 1
        i = 0
        j = 0
        sum = 0
        while i < len(nums):
            sum += nums[i]
            while sum - nums[j] >= target:
                sum -= nums[j]
                j += 1
            if sum >= target:
                res = min(res, i - j + 1)
            i += 1
        if res == 2**31 - 1:
            res = 0
        return res

    def minSubArrayLen_2(self, target, nums):
        res = 2**31 - 1
        i = 0
        j = 0
        sum = 0
        tmp = -1
        while i < len(nums):
            sum += nums[i]
            while sum - nums[j] >= target:
                sum -= nums[j]
                j += 1
            if sum >= target:
                res = min(res, i - j + 1)
                tmp = i
            i += 1
        if res == 2 ** 31 - 1:
            return []
        return nums[tmp - res + 1 : tmp + 1]


solution = Solution()
# print(solution.minSubArrayLen_2(7, [2,3,1,2,4,3]))
# print(solution.minSubArrayLen_2(4, [1,4,4]))
print(solution.minSubArrayLen_2(11, [1, 1, 1, 1, 1, 1, 1, 1]))
