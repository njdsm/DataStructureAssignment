class Binary_Tree:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value
        self.root = value

    def add_node(self, new_data, root):
        if root is None:
            return Binary_Tree(new_data)
        else:
            if new_data == root.value:
                return root
            elif new_data > root.value:
                root.right = self.add_node(new_data, root.right)
            else:
                root.left = self.add_node(new_data, root.left)
        return root

    def search_for_node(self, value, root):
        if root is None:
            return False
        elif root.value == value:
            return True
        else:
            if value > root.value:
                return self.search_for_node(value, root.right)
            else:
                return self.search_for_node(value, root.left)

