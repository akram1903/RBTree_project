from red_black_node import RBNode


class RBTree:
    root = None
    length = 1

    def __init__(self, root):
        self.root = root

    def __search_inner(self, value, relative_root):
        # search the node with the value in parameter then returns the node parent and a flag=1 if found and 0 otherwise
        if relative_root is None:       # what the heck is that
            print("__________ search inner error __________")
            print("rel_root in the function is None")

        elif relative_root.value == value:
            return [relative_root.parent, 1]
        elif relative_root.value > value:
            if relative_root.left is None:
                return relative_root
            else:
                return self.__search_inner(value, relative_root.left)

        else:
            if relative_root.right is None:
                return relative_root
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
        print("Traversing tree:\n\n")

        self.__traverse_inner(self.root, 0)
        pass

    def get_depth_naiveBST(self):
        print("\n\n")
        result = self.__get_depth_naiveBST(self.root, 1, 0)
        return result

    def __get_depth_naiveBST(self, rel_root, l, max_depth):
        if rel_root is None:
            return max_depth
        if rel_root.left is not None:
            print(str(l+1)+'\t'+str(max_depth))
            if l+1 > max_depth:
                max_depth = self.__get_depth_naiveBST(rel_root.left, l + 1, l + 1)
            else:
                max_depth = self.__get_depth_naiveBST(rel_root.left, l + 1, max_depth)
        if rel_root.right is not None:
            print(str(l + 1) + '\t' + str(max_depth))
            if l + 1 > max_depth:
                max_depth = self.__get_depth_naiveBST(rel_root.right, l + 1, l + 1)
            else:
                max_depth = self.__get_depth_naiveBST(rel_root.right, l + 1, max_depth)

        return max_depth

    def get_depth_RB(self):
        return self.__get_depth_RB(self.root, 1, 0)

    def __get_depth_RB(self, rel_root, l, max_depth):
        if rel_root is None:
            return max_depth
        if rel_root.isBlack():
            l += 1
        if rel_root.left is not None:
            # print(str(l) + '\t' + str(max_depth))
            if l > max_depth:
                max_depth = self.__get_depth_naiveBST(rel_root.left, l, l)
            else:
                max_depth = self.__get_depth_naiveBST(rel_root.left, l, max_depth)
        if rel_root.right is not None:
            # print(str(l) + '\t' + str(max_depth))
            if l > max_depth:
                max_depth = self.__get_depth_naiveBST(rel_root.right, l, l)
            else:
                max_depth = self.__get_depth_naiveBST(rel_root.right, l, max_depth)

        return max_depth

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

    def __traversal_properties(self, root, flags):
        # leaf property
        if root.right is None and root.left is None:
            if not root.isBlack:
                flags[0] = True
        # red property
        if (root is not None) and (not root.isBlack):
            if (root.parent is not None) and (not root.isBlack):
                flags[1] = True

        # depth property


    def check_traversal_properties(self):
        flags = []
        self.__traversal_properties(self.root, flags)
        return flags

    def check_red_black_tree(self):
        flags = [False, False, False, False]
        # [root property, leaf property, red property, depth property]
        # true means rule violated false means rule not violated

        if not self.root.isblack:
            flags[0] = True

        flags = [flags[0], self.check_traversal_properties()]


