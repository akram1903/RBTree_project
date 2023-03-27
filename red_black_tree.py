from red_black_node import RBNode


class RBTree:
    root = None
    length = 1

    def __init__(self, root):
        self.root = root

    def __search_inner(self, value, relative_root):
        if relative_root is None:
            return [relative_root.parent, 0]
        elif relative_root.value == value:
            return [relative_root.parent, 1]
        elif relative_root.value > value:
            return self.__search_inner(value, relative_root.left)
        else:
            return self.__search_inner(value, relative_root.right)

    def search(self, value):
        return self.__search_inner(value, self.root)

    def __traverse_inner(self, relative_root, depth):
        if relative_root is not None:
            for i in range(depth, 0, -1):
                print('\t', end='')
            print(relative_root)

        if relative_root.left is not None:
            self.__traverse_inner(relative_root.left, depth+1)

        if relative_root.right is not None:
            self.__traverse_inner(relative_root.right, depth+1)
        pass

    def traverse(self):
        self.__traverse_inner(self.root, 0)
        pass

    def get_length(self):
        return self.__get_length(self.root, 1)

    def __get_length(self, rel_root, l):
        if rel_root is None:
            return 0
        elif rel_root.left is not None:
            return self.__get_length(rel_root.left, l+1)
        else:
            return l

    def insert_bst(self, node):
        self.__insert_bst(node, self.root)
        pass

    def __insert_bst(self, node, root):
        if root.value > node.value:
            if root.left is None:
                root.left = node
                node.parent = root
            else:
                self.__insert_bst(node, root.left)
        elif root.value < node.value:
            if root.right is None:
                root.right = node
                node.parent = root
            else:
                self.__insert_bst(node, root.right)

    def insert_rb_naive(self, value):

        search = self.search(value)
        if search[1] == 1:
            print("node already exists")
            pass
        parent = search[0]
        node = RBNode(value, parent)

        if parent.value > value:
            parent.left = node
        else:
            parent.right = node


