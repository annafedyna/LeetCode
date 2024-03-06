class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def reverseList(self, head):
        if not head or  not head.next:
            return head
        
        t = head.next   
        head.next = None
        reversed_tail = self.reverseList(t)
        t.next = head
        return reversed_tail 
    
s = Solution()
print(s.reverseList(ListNode(1,ListNode(2,ListNode(3, ListNode(4, ListNode(5)))))))

# SOLUTION 2

class Solution2:
    def reverseList(self, head):
        
        return 