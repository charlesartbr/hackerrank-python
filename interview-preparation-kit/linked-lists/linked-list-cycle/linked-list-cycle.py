def has_cycle(head):
    
    datas = []
    current = head
    
    while current:

        if current.data in datas:
            return 1
        else:
            datas.append(current.data)

        current = current.next

    return 0