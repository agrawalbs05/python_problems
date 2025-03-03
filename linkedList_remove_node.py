# Remove Linked List Elements
# Tags : N203, Blind75, linkedList, Easy
# Input: head = [1,2,6,3,4,5,6], val = 6
# Output: [1,2,3,4,5]

def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        
    dummy = ListNode(next=head)
    prev,curr = dummy,head
        
    while curr:
        if curr.val == val:
            prev.next = curr.next #delete value by pointing next
        else:
            prev = curr #If not deleting then shifted to right
        curr = curr.next
        
    return dummy.next #Always return dummy next as we are not deleting it
        
    # Time complexity : O(n)
    # Space complexity : O(1)

head = [1,2,6,3,4,5,6]
val = 6
removeElements(head,val)