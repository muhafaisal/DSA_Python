def compare_lists(llist1, llist2):
    temp1 = llist1
    temp2 = llist2
    
    while temp1 is not None and temp2 is not None and temp1.data == temp2.data:
        temp1 = temp1.next
        temp2 = temp2.next
        if temp1 is None and temp2 is None:
            return 1
    else:
        return 0
    return 1