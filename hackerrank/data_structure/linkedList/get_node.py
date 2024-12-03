def getNode(llist, positionFromTail):
    count = 0
    temp = llist
    while temp:
        count += 1
        temp = temp.next
    if count == 1:
        return llist.data
    else:
        for _ in range(count -1 -positionFromTail):
            llist = llist.next
        return llist.data