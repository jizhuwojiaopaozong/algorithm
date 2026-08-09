from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        res = []
        for i in nums:
            if not res or i > res[-1]:
                res.append(i)
            else:
                if i <= res[0]:
                    res[0] = i
                else:
                    l = 0
                    r = len(res) - 1
                    while l < r:
                        mid = (l + r + 1) // 2
                        if res[mid] < i:
                            l = mid
                        else:
                            r = mid - 1
                    res[r + 1] = i
        return len(res)

    def lengthOfLIS_1(self, nums: List[int]) -> int:
        res = []
        prev = [-1] * len(nums)
        for id, val in enumerate(nums):
            if not res or val > nums[res[-1]]:
                if res:
                    prev[id] = res[-1]
                res.append(id)
            else:
                if val <= nums[res[0]]:
                    res[0] = id
                else:
                    l = 0
                    r = len(res) - 1
                    while l < r:
                        mid = (l + r + 1) // 2
                        if nums[res[mid]] < val:
                            l = mid
                        else:
                            r = mid - 1
                    prev[id] = res[r]
                    res[r + 1] = id
        ans = []
        cur = res[-1]
        while cur != -1:
            ans.append(nums[cur])
            cur = prev[cur]
        return ans[::-1]


# 为什么 res 可以不是真实子序列？
# 这个算法叫耐心排序（Patience Sorting），它维护的 res[i] 表示：
# 长度为 i+1 的递增子序列，其结尾元素的最小可能值。

# 因为 res 只关心结尾元素的最小可能值，所以它不需要是真实子序列。
# 例如，[10,9,2,5,3,7,101,18] 的 res 可以是 [2,3,7,101]，
# 因为 2,3,7,101 是长度为 4 的递增子序列，其结尾元素的最小可能值是 2,3,7,101。
# 但是 2,3,7,101 不是真实子序列，因为 10,9,2,5,3,7,101,18 的递增子序列是 [2,3,7,101]。
# 所以 res 可以不是真实子序列。

# 它用不保持原顺序的最小结尾值来换取了高效的 O(n log n) 长度计算。只要记住 res 只是一个“长度相等的占位符”而不是真实序列，就不会被它的内容迷惑了。

solution = Solution()
print(solution.lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]))
print(solution.lengthOfLIS([0, 1, 0, 3, 2, 3]))
print(solution.lengthOfLIS([7, 7, 7, 7, 7, 7, 7]))
print(solution.lengthOfLIS_1([10, 9, 2, 5, 3, 7, 101, 18]))
print(solution.lengthOfLIS_1([0, 1, 0, 3, 2, 3]))
print(solution.lengthOfLIS_1([7, 7, 7, 7, 7, 7, 7]))
print(solution.lengthOfLIS_1([0, 1, 2, 3, -1]))