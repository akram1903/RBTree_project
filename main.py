
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


node1.changeColor()
node10.changeColor()
node20.changeColor()
node2.changeColor()
node8.changeColor()
node3.changeColor()
node5.changeColor()
node4.changeColor()
# https://github.com/akram1903/RBTree_project.git

tree1 = RBTree(node5)
tree1.insert_bst(node2)
tree1.insert_bst(node10)
# tree1.insert_bst(node1)
tree1.insert_bst(node3)
# tree1.insert_bst(node8)
tree1.insert_bst(node20)
# tree1.insert_bst(node4)

tree1.traverse()
print()
print("Tree depth is  "+str(tree1.get_depth_RB()))
print()
tree1.check_red_black_tree()
tree1.print2D(tree1.root)
print()
print(tree1.get_total_size())