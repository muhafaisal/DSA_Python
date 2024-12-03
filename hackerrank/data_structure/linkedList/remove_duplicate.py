def removeDuplicates(llist):
    arr = []
    while llist:
        arr.append(llist.data)
        llist = llist.next
    arr = list(set(arr))
   
    temp = SinglyLinkedListNode(-1)
    head = temp
    
    for i in arr:
        new_node = SinglyLinkedListNode(i)
        temp.next = new_node
        temp = new_node
    head = head.next
    
    return head