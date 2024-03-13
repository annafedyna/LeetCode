
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
        

def pairSum(head) -> int:
    
    list = []
    
    while head:
        list.append(head.val)
        head = head.next
    
    return max([list[i] + list[len(list)-1-i] for i in range(len(list)//2)])
    
print(pairSum(ListNode(5,ListNode(4,ListNode(2,ListNode(1))))))