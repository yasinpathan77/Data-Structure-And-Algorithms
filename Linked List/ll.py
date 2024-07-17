
class Node:
    def __init__(self, value) -> None:
        self.Value = value
        self.next = None


class LinkedList:

    def __init__(self) -> None:
        self.length = 0
        self.head = None
        self.tail = None

    def __init__(self, value) -> None:
        newNode = Node(value)
        self.tail = newNode
        self.head = newNode
        self.length = 1

    def print(self) -> None:
        pointer = self.head
        while pointer:
            print(pointer.Value)
            pointer = pointer.next

    def append(self, value) -> None:
        newNode = Node(value)
        if self.length == 0:
            self.head = newNode
        else:
            self.tail.next = newNode
        self.tail = newNode
        self.length += 1




ll = LinkedList(4)

ll.append(7)

ll.print()

print('Head', ll.head.Value)
print('Tail', ll.tail.Value)
print('Length', ll.length)
