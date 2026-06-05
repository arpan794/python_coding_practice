class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# transverse and print linked list

def transverse(head):
    curr = head
    while curr:
        print(curr.data, end="->")
        curr = curr.next
    print("null")

# find the lowest

def lowest(head):
    curr = head.next
    lowest = head.data
    while curr:
        if lowest > curr.data:
            lowest = curr.data
        curr = curr.next
    return lowest


# delete the node

def del_node(head, node):
    curr = head
    while curr.next and curr.next != node:
        curr = curr.next

    if curr.next is None:
        return head
    
    curr.next = curr.next.next

    return head




