def mergeLists(head1, head2):
    arr = []
    while head1:
        arr.append(head1.data)
        head1 = head1.next
    
    while head2:
        arr.append(head2.data)
        head2 = head2.next

    arr.sort()

    temp = SinglyLinkedListNode(-1)
    head = temp
    for _ in arr:
        temp.next = SinglyLinkedListNode(_)
        temp = temp.next
    head = head.next

    return head