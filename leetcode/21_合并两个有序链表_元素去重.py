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
            while p.next:
                if p.next.value == p.value:
                    p = p.next
                else:
                    break
            while q.next:
                if q.next.value == q.value:
                    q = q.next
                else:
                    break
            if p.value > q.value:
                cur.next = q
                cur = q
                q = q.next
            elif p.value < q.value:
                cur.next = p
                cur = p
                p = p.next
            else:
                cur.next = p
                cur = p
                p = p.next
                q = q.next
        if p:
            while p:
                while p.next:
                    if p.next.value == p.value:
                        p = p.next
                    else:
                        break
                cur.next = p
                cur = p
                p = p.next

        if q:
            while q:
                while q.next:
                    if q.next.value == q.value:
                        q = q.next
                    else:
                        break
                cur.next = q
                cur = q
                q = q.next
        return dummy.next

    def createLinkList(self, list):
        if len(list) == 0:
            return None
        head = LinkNode(list[0])
        cur = head
        for i in list[1:]:
            cur.next = LinkNode(i)
            cur = cur.next
        return head

    def printLinkList(self, head: LinkNode):
        res = []
        cur = head
        while cur:
            res.append(cur.value)
            cur = cur.next
        return res


solution = Solution()
# list1 = solution.createLinkList([1, 2, 4])
# list2 = solution.createLinkList([1, 3, 4])
# ans = solution.mergeTwoLists(list1, list2)
# print(solution.printLinkList(ans))

# list1 = solution.createLinkList([1, 1, 2, 2, 3, 3, 4])
# list2 = solution.createLinkList([1, 1, 3, 3, 3, 4, 4, 4, 5])
# ans = solution.mergeTwoLists(list1, list2)
# print(solution.printLinkList(ans))


# list1 = solution.createLinkList([])
# list2 = solution.createLinkList([])
# ans = solution.mergeTwoLists(list1, list2)
# print(solution.printLinkList(ans))


# list1 = solution.createLinkList([])
# list2 = solution.createLinkList([0, 0, 0, 0])
# ans = solution.mergeTwoLists(list1, list2)
# print(solution.printLinkList(ans))

list1 = solution.createLinkList([])
list2 = solution.createLinkList([0])
ans = solution.mergeTwoLists(list1, list2)
print(solution.printLinkList(ans))
