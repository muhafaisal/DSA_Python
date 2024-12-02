def reversePrint(llist):
    count = 0
    node = llist
    while node:
        count = count + 1 
        node = node.next
        
    if count == 0:
        return None
        
    for i in range (count):
        curr = llist
        for _ in range (count - i -1):
            curr = curr.next
        print(curr.data)