from queue import Queue


class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class Solution:
    def lowestCommonAncestor(
        self, root: TreeNode, p: TreeNode, q: TreeNode
    ) -> TreeNode:
        if not root:
            return None
        if root == p or root == q:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if left and right:
            return root
        if left:
            return left
        return right

    def createTreeNode(self, nums):
        if len(nums) == 0:
            return None
        root = TreeNode(nums[0])
        q = Queue()
        q.put(root)
        i = 1
        node_map = {nums[0]: root}
        while not q.empty() and i < len(nums):
            size = q.qsize()
            while size:
                size -= 1
                tmp = q.get()
                if i < len(nums) and nums[i] is not None:
                    tmp.left = TreeNode(nums[i])
                    q.put(tmp.left)
                    node_map[nums[i]] = tmp.left
                i += 1
                if i < len(nums) and nums[i] is not None:
                    tmp.right = TreeNode(nums[i])
                    q.put(tmp.right)
                    node_map[nums[i]] = tmp.right
                i += 1
        return root, node_map


solution = Solution()
root, node_map = solution.createTreeNode([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4])
p = node_map[5]
q = node_map[1]
print(solution.lowestCommonAncestor(root, p, q).value)

root, node_map = solution.createTreeNode([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4])
p = node_map[5]
q = node_map[4]
print(solution.lowestCommonAncestor(root, p, q).value)

root, node_map = solution.createTreeNode([1, 2])
p = node_map[1]
q = node_map[2]
print(solution.lowestCommonAncestor(root, p, q).value)