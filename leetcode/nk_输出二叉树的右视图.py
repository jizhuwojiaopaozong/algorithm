from typing import List
from queue import Queue


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def preOrderInOrder(self, preOrder: List[int], inOrder: List[int]) -> TreeNode:
        if not preOrder or not inOrder:
            return None
        d = {v: k for k, v in enumerate(inOrder)}

        def dfs(pre_left, pre_right, in_left, in_right):
            if pre_left > pre_right:
                return None
            root = TreeNode(preOrder[pre_left])
            in_index = d[root.val]
            tmp = in_index - in_left
            root.left = dfs(pre_left + 1, pre_left + tmp, in_left, in_index - 1)
            root.right = dfs(pre_left + tmp + 1, pre_right, in_index + 1, in_right)
            return root

        return dfs(0, len(preOrder) - 1, 0, len(inOrder) - 1)

    def InOrderPostOrder(self, inOrder: List[int], postOrder: List[int]) -> TreeNode:
        if not inOrder or not postOrder:
            return None
        d = {v: k for k, v, in enumerate(inOrder)}

        def dfs(in_left, in_right, post_left, post_right):
            if post_left > post_right:
                return None
            root = TreeNode(postOrder[post_right])
            index = d[root.val]
            tmp = index - in_left
            root.left = dfs(in_left, index - 1, post_left, post_left + tmp - 1)
            root.right = dfs(index + 1, in_right, post_left + tmp, post_right - 1)
            return root

        return dfs(0, len(inOrder) - 1, 0, len(postOrder) - 1)

    def solve(self, inOrder: List[int], postOrder: List[int]) -> List[int]:
        # root = self.preOrderInOrder(preOrder, inOrder)
        root = self.InOrderPostOrder(inOrder, postOrder)
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


sol = Solution()
# print(sol.solve([1, 2, 4, 5, 3], [4, 2, 5, 1, 3]))
# print(sol.solve([1, 2, 4, 5, 3, 6, 7], [4, 2, 5, 1, 6, 3, 7]))

print(sol.solve([4, 2, 5, 1, 3], [4, 5, 2, 3, 1]))
