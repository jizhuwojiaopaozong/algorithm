class LinkNode:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class Solution:
    def reverseKGroup(self, head: LinkNode, k:int) -> LinkNode:
        dummy = LinkNode(-1)
        dummy.next = head
        p = dummy
        while p:
            q = p
            for i in range(k):
                if q:
                    q = q.next
            if not q:
                break
            a = p.next
            b = a.next
            for j in range(k-1):
                c = b.next
                b.next = a
                a = b
                b = c
            d = p.next
            d.next = b
            p.next = a
            p = d
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
ans = solution.reverseKGroup(head, 4)
print(solution.printLinkNode(ans))