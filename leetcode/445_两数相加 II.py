class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        def reverse_list(head: ListNode) -> ListNode:
            a = head
            b = a.next
            a.next = None
            while b:
                c = b.next
                b.next = a
                a = b
                b = c
            return a

        l1 = reverse_list(l1)
        l2 = reverse_list(l2)
        dummy = ListNode(-1)
        cur = dummy
        t = 0
        while l1 or l2 or t:
            if l1:
                t += l1.val
                l1 = l1.next
            if l2:
                t += l2.val
                l2 = l2.next
            cur.next = ListNode(t % 10)
            cur = cur.next
            t //= 10
        cur.next = None
        return reverse_list(dummy.next)

    # 非反转链表用栈实现
    def addTwoNumbers1(self, l1: ListNode, l2: ListNode) -> ListNode:
        sk1 = []
        sk2 = []
        while l1:
            sk1.append(l1.val)
            l1 = l1.next
        while l2:
            sk2.append(l2.val)
            l2 = l2.next
        dummy = ListNode(-1)
        t = 0
        while sk1 or sk2 or t:
            if sk1:
                t += sk1.pop()
            if sk2:
                t += sk2.pop()
            node = ListNode(t % 10)
            t //= 10
            node.next = dummy.next
            dummy.next = node
        return dummy.next
