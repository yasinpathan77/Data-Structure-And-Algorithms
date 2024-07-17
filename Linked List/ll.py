class Node:
    def __init__(self, value) -> None:
        self.Value = value
        self.next = None


class LinkedList:
    def __init__(self, value) -> None:
        newNode = Node(value)
        self.tail = newNode
        self.head = newNode
        self.length = 1


ll = LinkedList(4)

print('Head', ll.head.Value)
print('Tail', ll.tail.Value)
print('Length', ll.length)
