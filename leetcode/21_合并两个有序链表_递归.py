class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        if list1 is None:
            return list2
        if list2 is None:
            return list1
        if list1.val < list2.val:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        else:
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2

    def createListNode(self, nums):
        if len(nums) == 0:
            return None
        head = ListNode(nums[0])
        cur = head
        for i in nums[1:]:
            cur.next = ListNode(i)
            cur = cur.next
        return head
    
    def printListNode(self, head):
        cur = head
        res = []
        while cur:
            res.append(cur.val)
            cur = cur.next
        return res

solution = Solution()
list1 = solution.createListNode([1,2,4])
list2 = solution.createListNode([1,3,4])
result = solution.mergeTwoLists(list1, list2)
print(solution.printListNode(result))