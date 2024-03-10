
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        

def oddEvenList(head):
    if not head:
        return None 
    

    dummy = ListNode()
    even = ListNode()
    
    
    odd = True
    
    dummy_head = dummy
    even_head = even
    
    
    while head:
        if odd:
            dummy.next = head
            dummy = dummy.next
        else:
            even.next = head
            even = even.next
            
        odd = not odd
        head = head.next
        
    dummy.next = even_head.next
    even.next = None # to escape loops
    
    return dummy_head.next
    
    
print(oddEvenList(ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))))
        