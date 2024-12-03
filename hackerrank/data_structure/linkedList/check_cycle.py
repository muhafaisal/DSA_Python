def has_cycle(head):
    st = set() 
    while head: 
        if head in st:
            return 1
        st.add(head)
        head = head.next
    return 0