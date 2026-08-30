from typing import List
from queue import Queue


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        res = []
        if not root:
            return res
        q = Queue()
        q.put(root)
        while not q.empty():
            size = q.qsize()
            while size:
                size -= 1
                tmp = q.get()
                if not size:
                    res.append(tmp.val)
                if tmp.left:
                    q.put(tmp.left)
                if tmp.right:
                    q.put(tmp.right)
        return res

    def createTreeNode(self, nums: List[int]) -> TreeNode:
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

    def dfs(self, root: TreeNode) -> List[int]:
        res = []

        def dfs(node, depth):
            if not node:
                return
            if len(res) == depth:
                res.append(node.val)
            dfs(node.right, depth + 1)
            dfs(node.left, depth + 1)

        dfs(root, 0)
        return res


solution = Solution()
root = solution.createTreeNode([1, 2, 3, None, 5, None, 4])
print(solution.rightSideView(root))

root = solution.createTreeNode([1, 2, 3, 4, None, None, None, 5])
print(solution.rightSideView(root))


root = solution.createTreeNode([1, None, 3])
print(solution.rightSideView(root))


root = solution.createTreeNode([])
print(solution.rightSideView(root))
