class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def deleteMiddle(self, head):
        if not head: 
            return None

        if not head.next:
            return None
        
        prev = ListNode(0)
        r = head
        l = head
        
        while l.next and l.next.next:
            prev = r
            r = r.next
            l = l.next.next

        if l.next:
            r.next = r.next.next
        else: 
            prev.next = r.next
        return head
    
s = Solution() 
print(s.deleteMiddle(ListNode(1,ListNode(2,ListNode(3, ListNode(4, ListNode(5, ListNode(6))))))))