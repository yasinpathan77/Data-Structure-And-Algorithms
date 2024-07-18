class Node:
    """Class for node of linked list."""

    def __init__(self, value) -> None:
        """
        Initialize node.

        Args:
            value: Value to be stored in the node.
        """
        self.Value = value
        self.next = None


class LinkedList:
    """Class for singly linked list."""

    def __init__(self, value=None) -> None:
        """
        Initialize linked list.

        Args:
            value: Value of the first node, if provided.
        """
        self.length = 0
        self.head = None
        self.tail = None

        if value is not None:
            newNode = Node(value)
            self.tail = newNode
            self.head = newNode
            self.length = 1

    def print(self) -> None:
        """Print all elements of the linked list."""
        current_node = self.head

        while current_node:
            print(current_node.Value)
            current_node = current_node.next

    def append(self, value) -> None:
        """
        Append a new node to the end of the linked list.

        Args:
            value: Value to be stored in the new node.
        """
        newNode = Node(value)

        if self.length == 0:
            self.head = newNode
        else:
            self.tail.next = newNode

        self.tail = newNode
        self.length += 1

    def empty(self):
        """Empty the linked list."""
        self.tail = None
        self.head = None
        self.length = 0

    def pop(self):
        """Remove the last node from the linked list."""
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
        """
        Add a new node to the beginning of the linked list.

        Args:
            value: Value to be stored in the new node.
        """
        newNode = Node(value)
        self.length += 1

        if self.length == 1:
            self.tail = newNode
        else:
            newNode.next = self.head

        self.head = newNode

    def pop_first(self):
        """Remove the first node from the linked list."""
        if self.length == 0:
            return None

        self.head = self.head.next

        if self.length == 1:
            self.tail = None

        self.length -= 1

    def set_value(self, index, value):
        """
        Set the value of a node at a specific index.

        Args:
            index: Index of the node.
            value: New value to be set.
        """
        target_node = self.get(index)

        if target_node:
            target_node.Value = value

    def get(self, index):
        """
        Get the node at a specific index.

        Args:
            index: Index of the node.

        Returns:
            Node at the specified index, if it exists. Otherwise, None.
        """
        if self.check_index_value(index):
            return None

        current_node = self.head
        for i in range(index):
            current_node = current_node.next

        return current_node

    def check_index_value(self, index):
        """
        Check if an index is valid for the linked list.

        Args:
            index: Index to be checked.

        Returns:
            True if the index is invalid, False otherwise.
        """
        return index+1 > self.length or index < 0

    def insert(self, index, value):
        """
        Insert a new node at a specific index.

        Args:
            index: Index where the new node should be inserted.
            value: Value to be stored in the new node.
        """
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
        """
        Remove the first node with a specific value.

        Args:
            value: Value of the node to be removed.
        """
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
        """Reverse the linked list."""
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

    def middle_node(self) -> Node:
        """
        Returns the middle node

        Returns:
            _type_: Node
        """
        slow = self.head
        fast = self.head
        while slow and fast:
            slow = slow.next
            fast = fast.next.next
        return slow

    def has_loop(self) -> bool:
        """Checks whether the list contains loop or not

        Returns:
            bool: True if it contains
        """
        slow = self.head
        fast = self.head
        while slow and fast:
            if slow == fast:
                return True
            slow = slow.next
            fast = fast.next.next
        return False

    def remove_duplicate(self) -> None:
        """ Removes duplicate value from linked list.
        """
        current_node = self.head
        values = set()
        while current_node:
            previous_node = current_node
            if current_node.Value in values:
                previous_node.next = current_node.next
            values.add(current_node.Value)
            current_node = current_node.next

    def find_kth_from_the_end(self, k) -> Node:
        """find the kth node from the end

        Args:
            k (int): position from ending

        Returns:
            Node: Linked List Node
        """
        kth_node = self.head
        forward_node = self.head
        for i in range(k):
            if not forward_node.next:
                return None
            forward_node = forward_node.next

        while forward_node:
            forward_node = forward_node.next
            kth_node = kth_node.next

        return kth_node

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
ll.append(2)
ll.remove_duplicate()
ll.print()

print('Head', ll.head.Value)
print('Tail', ll.tail.Value)
print('Length', ll.length)
