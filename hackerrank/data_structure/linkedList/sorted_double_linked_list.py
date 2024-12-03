def sortedInsert(llist, data):
    new_node = DoublyLinkedListNode(data)

    if llist is None:
        return new_node

    if data <= llist.data:
        new_node.next = llist
        llist.prev = new_node
        return new_node

    curr = llist
    while curr.next is not None and curr.next.data < data:
        curr = curr.next

    new_node.next = curr.next
    if curr.next is not None:
        curr.next.prev = new_node
    curr.next = new_node
    new_node.prev = curr

    return llist