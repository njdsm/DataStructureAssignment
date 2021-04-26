from node import Node


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append_node(self, data):
        node = Node(data)

        if self.head is None:
            self.head = node
            self.tail = node
            return
        else:
            self.tail.next = node
            self.tail = self.tail.next

    def add_to_beginning(self, data):
        new_head = Node(data)
        new_head.next = self.head
        self.head = new_head

    def contains_node(self, node, data):
        b = False
        while node is not None:
            if node.data == data:
                b = True
            node = node.next
        return b
