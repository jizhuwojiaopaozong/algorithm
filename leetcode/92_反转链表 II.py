class LinkNode:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class Solution:
    def reverseBetween(self, head: LinkNode, left:int, right:int) -> LinkNode:
        dummy = LinkNode(-1)
        dummy.next = head
        p = dummy
        for i in range(left-1):
            p = p.next
        a = p
        b = a.next
        c = b.next
        for j in range(right-left):
            d = c.next
            c.next = b
            b = c
            c = d
        a.next.next = c
        a.next = b
        return dummy.next

    def createLinkNode(self, list):
        head = LinkNode(list[0])
        p = head
        for i in list[1:]:
            p.next = LinkNode(i)
            p = p.next
        return head

    def printLinkNode(self, head):
        res = []
        p = head
        while p:
            res.append(p.value)
            p = p.next
        return res

solution = Solution()
head = solution.createLinkNode([1,2,3,4,5])
ans = solution.reverseBetween(head, 2, 4)
print(solution.printLinkNode(ans))