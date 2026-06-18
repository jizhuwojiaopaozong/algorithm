class LinkNode:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class Solution:
    # 迭代法
    def reverseList1(self, head: LinkNode) -> LinkNode:
        prev = None
        cur = head
        while cur:
            ne = cur.next
            cur.next = prev
            prev = cur
            cur = ne
        return prev

    # 递归法
    def reverseList(self, head: LinkNode) -> LinkNode:
        if not head or not head.next:
            return head
        tail = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return tail


    def createLinkNode(self, list):
        head = LinkNode(list[0])
        cur = head
        for i in list[1:]:
            cur.next = LinkNode(i)
            cur = cur.next
        return head
    
    def printLinkNode(self, head:LinkNode):
        res = []
        cur = head
        while cur:
            res.append(cur.value)
            cur = cur.next
        print(res)

solution = Solution()
head = solution.createLinkNode([1,2,3,4,5])
# ans = solution.reverseList(head)
ans = solution.reverseList1(head)
solution.printLinkNode(ans)