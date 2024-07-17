
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

    def prepend(self, value):
        newNode = Node(value)
        self.length += 1

        if self.length == 1:
            self.tail = newNode
        else:
            newNode.next = self.head

        self.head = newNode

    def pop_first(self):
        if self.length == 0:
            return None

        self.head = self.head.next

        if self.length == 1:
            self.tail = None

        self.length -= 1

    def set_value(self, index, value):
        target_node = self.get(index)

        if target_node:
            target_node.Value = value

    def get(self, index):
        if self.check_index_value(index):
            return None

        current_node = self.head
        for i in range(index):
            current_node = current_node.next

        return current_node

    def check_index_value(self, index):
        return index+1 > self.length or index < 0

    def insert(self, index, value):
        if self.check_index_value(index):
            return None

        if index == 0:
            self.prepend(value)
            return

        if index == self.length:
            self.append(value)
            return

        newNode = Node(value)
        previous_node = self.get(index-1)

        newNode.next = previous_node.next
        previous_node.next = newNode
        self.length += 1

    def remove(self, value):
        current_node = self.head
        previous_node = self.head
        self.length -= 1

        if self.length == 0:
            self.head, self.tail = None, None
            return

        if self.head.Value == value:
            self.head = self.head.next
            return

        while current_node.next and current_node.Value != value:
            previous_node = current_node
            current_node = current_node.next

        previous_node.next = current_node.next
        current_node.next = None

    def reverse(self):
        current_node = self.head
        self.tail = self.head
        previous_node = None
        while current_node.next:
            next_node = current_node.next
            current_node.next = previous_node
            previous_node = current_node
            current_node = next_node
        current_node.next = previous_node
        self.head = current_node



ll = LinkedList(4)

ll.append(7)
ll.pop()
ll.prepend(9)
ll.pop_first()
ll.set_value(0, 1)
ll.append(6)
ll.insert(1, 2)
# ll.remove(2)
ll.reverse()

ll.print()

print('Head', ll.head.Value)
print('Tail', ll.tail.Value)
print('Length', ll.length)
