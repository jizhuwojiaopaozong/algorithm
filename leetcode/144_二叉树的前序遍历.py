from typing import List


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        stk = []
        res = []
        while root or stk:
            while root:
                res.append(root.val)
                stk.append(root)
                root = root.left
            root = stk[-1].right
            stk.pop(-1)
        return res

    def preorderTraversal_dfs(self, root: TreeNode) -> List[int]:
        res = []

        def dfs(root):
            if not root:
                return
            res.append(root.val)
            dfs(root.left)
            dfs(root.right)

        dfs(root)
        return res
