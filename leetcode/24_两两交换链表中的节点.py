class LinkNode:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class Solution:
    def swapPairs(self, head: LinkNode) -> LinkNode:
        dummy = LinkNode(-1)
        dummy.next = head
        p = dummy
        while p.next and p.next.next:
            a = p.next
            b = a.next
            p.next = b
            a.next = b.next
            b.next = a
            p = a
        return dummy.next

    def createLinkNode(self, nums):
        if len(nums) == 0:
            return None
        head = LinkNode(nums[0])
        cur = head
        for i in nums[1:]:
            cur.next = LinkNode(i)
            cur = cur.next
        return head

    def printLinkNode(self, head):
        res = []
        cur = head
        while cur:
            res.append(cur.value)
            cur = cur.next
        return res


sol = Solution()
# head = sol.createLinkNode([1, 2, 3, 4])
# res = sol.swapPairs(head)
# print(sol.printLinkNode(res))

head = sol.createLinkNode([1])
res = sol.swapPairs(head)
print(sol.printLinkNode(res))