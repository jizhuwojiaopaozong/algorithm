from typing import List
from queue import Queue

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        ans = 0

        def dfs(root):
            nonlocal ans
            if not root:
                return 0
            left = dfs(root.left)
            right = dfs(root.right)
            ans = max(ans, left + right)
            return max(left, right) + 1

        dfs(root)
        return ans

    def createTreeNode(self, nums:List[int])->TreeNode:
        if not nums or len(nums) == 0:
            return None
        root = TreeNode(nums[0])
        q = Queue()
        q.put(root)
        i = 1
        while not q.empty() and i < len(nums):
            size =  q.qsize()
            while size:
                size -= 1
                tmp = q.get()
                if i < len(nums) and nums[i] is not None:
                    tmp.left = TreeNode(nums[i])
                    q.put(tmp.left)
                i += 1
                if i < len(nums) and nums[i] is not None:
                    tmp.right = TreeNode(nums[i])
                    q.put(tmp.right)
                i += 1
        return root


s = Solution()
nums = [1,2,3,4,5]
root = s.createTreeNode(nums)
print(s.diameterOfBinaryTree(root))


nums = [1,2,None,3,None,4,None,5]
root = s.createTreeNode(nums)
print(s.diameterOfBinaryTree(root))


nums = [1,2]
root = s.createTreeNode(nums)
print(s.diameterOfBinaryTree(root))