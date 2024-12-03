def findMergeNode(head1, head2):
    while head2 is not None:
        temp = head1
        
        while temp is not None:
            if temp is head2:
                return head2.data
            temp = temp.next
        head2 = head2.next
        
    return None