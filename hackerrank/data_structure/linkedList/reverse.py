def reverse(llist):
    curr = llist
    prev = None
    
    while curr is not None:
        new_node = curr.next
        curr.next = prev
        prev = curr
        curr = new_node
    return prev