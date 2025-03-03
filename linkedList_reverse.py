# Reverse Linked List
# Tags : N206, Blind75, linkedList, Easy

def reverseList(head):
        
    # Two pointer method.
    prev = None
    curr = head

    while curr:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp
    return prev
    #Time complexity O(n) and space complexity is O(1)    

head = [1,2,3,4,5]
reverseList(head)
