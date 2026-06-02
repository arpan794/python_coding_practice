class Node:
    def __init__(self, data=0):
        self.data = data
        self.next = next


def link_cycle(self, head: Node):
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False