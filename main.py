
from red_black_tree import RBTree
from red_black_node import RBNode
node1 = RBNode(1, None)
node2 = RBNode(2, None)
node3 = RBNode(3, None)
node4 = RBNode(4, None)
node5 = RBNode(5, None)
node10 = RBNode(10, None)
node20 = RBNode(20, None)
node8 = RBNode(8, None)
# node1.left = node2
# node1.right = node3
# node2.left = node4
# node2.right = node5

tree1 = RBTree(node10)
tree1.insert_bst(node1)
tree1.insert_bst(node5)
tree1.insert_bst(node3)
tree1.insert_bst(node4)
tree1.insert_bst(node2)
tree1.insert_bst(node20)
tree1.insert_bst(node8)

tree1.traverse()

print(tree1.get_depth_naiveBST())
