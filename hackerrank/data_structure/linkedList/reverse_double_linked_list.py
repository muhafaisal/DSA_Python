def reverse(llist):
    if llist is None or llist.next is None:
        return llist

    prev = None
    curr = llist
    
    while curr is not None:
        prev = curr.prev
        curr.prev = curr.next
        curr.next = prev
        curr = curr.prev

    return prev.prev