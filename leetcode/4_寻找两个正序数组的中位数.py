from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        def cal(nums1, i, nums2, j, k):
            if len(nums1) - i > len(nums2) - j:
                return cal(nums2, j, nums1, i, k)
            if k == 1:
                if i == len(nums1):
                    return nums2[j]
                else:
                    return min(nums1[i], nums2[j])
            if i == len(nums1):
                return nums2[j + k - 1]
            si = min(len(nums1), i + k // 2)
            sj = j + k - k // 2
            if nums1[si - 1] > nums2[sj - 1]:
                return cal(nums1, i, nums2, sj, k - (sj - j))
            else:
                return cal(nums1, si, nums2, j, k - (si - i))

        n = len(nums1)
        m = len(nums2)
        if (n + m) % 2:
            return cal(nums1, 0, nums2, 0, (n + m) // 2 + 1)
        else:
            left = cal(nums1, 0, nums2, 0, (n + m) // 2)
            right = cal(nums1, 0, nums2, 0, (n + m) // 2 + 1)
            return (left + right) / 2


sol = Solution()
print(sol.findMedianSortedArrays([1, 3], [2]))
print(sol.findMedianSortedArrays([1, 2], [3, 4]))
