from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        res_head = ListNode()
        res = res_head
        rest = 0
        while l1 is not None and l2 is not None:
            res.val = (l1.val + l2.val + rest) % 10
            rest = (l1.val + l2.val + rest) // 10
            l1 = l1.next
            l2 = l2.next
            if l1 or l2:
                res.next = ListNode()
                res = res.next

        while l1 is not None:
            res.val = (l1.val + rest) % 10
            rest = (l1.val + rest) // 10
            l1 = l1.next
            if l1:
                res.next = ListNode()
                res = res.next
        
        while l2 is not None:
            res.val = (l2.val + rest) % 10
            rest = (l2.val + rest) // 10
            l2 = l2.next
            if l2:
                res.next = ListNode()
                res = res.next

        if rest:
            res.next = ListNode()
            res = res.next
            res.val = rest
        return res_head 


    def traverseList(self, head):
        while head is not None:
            print(head.val, end="")
            if head.next is not None:   
                print(" -> ", end="")
            head = head.next
        print()


l1 = ListNode(2, ListNode(4))
l2 = ListNode(5, ListNode(6, ListNode(4)))

sol = Solution()
result = sol.addTwoNumbers(l1, l2)
sol.traverseList(result)
