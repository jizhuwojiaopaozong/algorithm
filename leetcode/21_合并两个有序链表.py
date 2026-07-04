class LinkNode:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: LinkNode, list2: LinkNode) -> LinkNode:
        dummy = LinkNode(-1)
        cur = dummy
        p = list1
        q = list2
        while p and q:
            if p.value < q.value:
                cur.next = p
                cur = p
                p = p.next
            else:
                cur.next = q
                cur = q
                q = q.next
        if p:
            cur.next = p
        if q:
            cur.next = q
        return dummy.next

    def createLinkNode(self, list):
        if len(list) == 0:
            return None
        head = LinkNode(list[0])
        cur = head
        for i in list[1:]:
            cur.next = LinkNode(i)
            cur = cur.next
        return head

    def printLinkNode(self, head: LinkNode):
        cur = head
        res = []
        while cur:
            res.append(cur.value)
            cur = cur.next
        return res


solution = Solution()
# list1 = solution.createLinkNode([1, 2, 4])
# list2 = solution.createLinkNode([1, 3, 4])
# ans = solution.mergeTwoLists(list1, list2)
# print(solution.printLinkNode(ans))
# list1 = solution.createLinkNode([])
# list2 = solution.createLinkNode([])
# ans = solution.mergeTwoLists(list1, list2)
# print(solution.printLinkNode(ans))
list1 = solution.createLinkNode([])
list2 = solution.createLinkNode([0])
ans = solution.mergeTwoLists(list1, list2)
print(solution.printLinkNode(ans))
