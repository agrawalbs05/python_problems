# Detect Linked List cycle
# Tags : N141, Blind75, linkedList, Easy

def hasCycle(head):

    # Can use Tortoise and Hare logic.If T and H are meeting each other then there is cycle as T is twice as H
    # Initially both ponitera at same location
    T = head
    H = head

    while T and T.next:
        H = H.next
        T = T.next.next
        if H == T:
            return True
    return False

    # Liner time and constant space. T O(n), S O(1)

head = [3,2,0,-4]
pos = 1
hasCycle(head)
