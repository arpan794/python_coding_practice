# reverse linked list

class Node:
    def __init__(self,data=0):
        self.data = data
        self.next = None

head = Node(7)
node1 = Node(1)
node2 = Node(2)

head.next = node1
node1.next = node2

def reverse_linked_list(head):
    curr = head
    prev = None
    while curr:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
    return prev
    

prev = reverse_linked_list(head)

curr = prev
while curr:
    print(curr.data)
    curr = curr.next

