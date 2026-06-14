from typing import List


class Solution:
    ## 暴力枚举
    def twoSum_1(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        for i in range(n):
            for j in range(i+1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return [-1, -1]
    
    ## 哈希表
    def twoSum_2(self, nums: List[int], target: int) -> List[int]:
        if not nums or len(nums) < 2:
            return [-1, -1]
        d = {}
        for i, num in enumerate(nums):
            remain = target - num
            if remain in d:
                return [d[remain], i]
            d[num] = i
        return [-1, -1]

    
    ## 两数之和 变形题（数组有重复数字，需要输出所有符合要求的数字对）（https://juejin.cn/post/7337225888265338934）
    ## 输入：[3, 3, 3, 4, 2, 3], 6
    ## 输出：[[3, 3], [3, 3], [3, 3], [4, 2], [3, 3], [3, 3], [3, 3]]
    def twoSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        d = {}
        for i, num in enumerate(nums):
            remain = target - num
            if remain in d:
                for ii in d[remain]:
                    res.append([nums[ii], num])
            if num in d:
                d[num].append(i)
            else:
                d[num] = [i]
        return res     

    
solution = Solution()
print(solution.twoSum([3, 3, 3, 4, 2, 3], 6))