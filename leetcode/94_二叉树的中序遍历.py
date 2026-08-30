from queue import Queue
from typing import List


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res = []

        def dfs(root):
            if not root:
                return
            dfs(root.left)
            res.append(root.val)
            dfs(root.right)

        dfs(root)
        return res

    def inorderTraversal_iterative(self, root: TreeNode) -> List[int]:
        stk = []
        res = []
        while root or stk:
            while root:
                stk.append(root)
                root = root.left
            if stk:
                res.append(stk[-1].val)
                root = stk[-1].right
                stk.pop(-1)
        return res

    def createTree(self, nums: List[int]) -> TreeNode:
        if not nums or len(nums) == 0:
            return None
        root = TreeNode(nums[0])
        q = Queue()
        q.put(root)
        i = 1
        while not q.empty() and i < len(nums):
            size = q.qsize()
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


solution = Solution()
root = solution.createTree([1, None, 2, 3])
print(solution.inorderTraversal(root))
print(solution.inorderTraversal_iterative(root))


root = solution.createTree([])
print(solution.inorderTraversal(root))
print(solution.inorderTraversal_iterative(root))


root = solution.createTree([1])
print(solution.inorderTraversal(root))
print(solution.inorderTraversal_iterative(root))
