
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
        current_node = self.head
        while current_node:
            print(current_node.Value)
            current_node = current_node.next

    def append(self, value) -> None:
        newNode = Node(value)
        if self.length == 0:
            self.head = newNode
        else:
            self.tail.next = newNode
        self.tail = newNode
        self.length += 1

    def empty(self):
        self.tail = None
        self.head = None
        self.length = 0

    def pop(self):
        if self.length == 0:
            return None
        current_node = self.head
        while current_node.next:
            previous_node = current_node
            current_node = current_node.next
        self.length -= 1
        if self.length == 0:
            self.head, self.tail = None, None
        self.tail = previous_node
        previous_node.next = None

ll = LinkedList(4)

ll.append(7)
ll.pop()
ll.print()

print('Head', ll.head.Value)
print('Tail', ll.tail.Value)
print('Length', ll.length)
