class Node(object):

    def __init__(self, data):
        """Initialize this node with the given data."""
        self.data = data
        self.next = None

    def __repr__(self):
        """Return a string representation of this node."""
        return 'Node({!r})'.format(self.data)


class LinkedList(object):

    def __init__(self, items=None):
        """Initialize this linked list and append the given items, if any."""
        self.head = None  # First node
        self.tail = None  # Last node
        # Append given items
        if items is not None:
            for item in items:
                self.append(item)

    def __str__(self):
        """Return a formatted string representation of this linked list."""
        items = ['({!r})'.format(item) for item in self.items()]
        return '[{}]'.format(' -> '.join(items))

    def __repr__(self):
        """Return a string representation of this linked list."""
        return 'LinkedList({!r})'.format(self.items())

    def items(self):
        """Return a list (dynamic array) of all items in this linked list"""
        items = []

        node = self.head

        while node is not None:
            items.append(node.data)

            node = node.next

        return items

    def is_empty(self):
        """Return a boolean indicating whether this linked list is empty."""
        return self.head is None

    def length(self):
        """Return the length of this linked list by traversing its nodes"""

        length = 0
        node = self.head

        while node is not None:
            length += 1

            node = node.next
        return length

    def append(self, item):
        """Insert the given item at the tail of this linked list"""

        node = Node(item)

        if self.tail is not None:
            self.tail.next = node
        else:
            self.head = node
        self.tail = node

    def prepend(self, item):
        """Insert the given item at the head of this linked list"""

        node = Node(item)
        if self.head is not None:
            node.next = self.head
        else:
            self.tail = node
        self.head = node

    def find(self, quality):
        """Return an item from this linked list """

        node = self.head
        while node is not None:
            if quality(node.data):
                return node.data

            node = node.next
        return None
    def delete(self, item):
        """Delete the given item from this linked list, or raise ValueError.
        TODO: Best case running time: O(2) List is empty:
            O(1) to check head is not None (false)
            O(1) to raise error
        TODO: Worst case running time: O(n) Item is last:
            Loop through all nodes, then reassign tail and previous_node.next
            """
        if self.head is not None:  # constant time for comparison
            previous_node = None
            node = self.head
            while node is not None:  # n iterations
                if node.data == item:
                    if previous_node is not None:
                        previous_node.next = node.next
                    else:
                        self.head = node.next
                    if node.next is None:  # last item
                        self.tail = previous_node
                    return

                previous_node = node
                node = node.next
        raise ValueError('Item not found: {}'.format(item))

    def replace(self, item, new_item):
        """Replace item with new_item."""
        node = self.head
        while node is not None:
            if item == node.data:
                node.data = new_item
                return

            node = node.next
        raise ValueError('Item not found: {}'.format(item))


if __name__ == '__main__':
    test_linked_list()
