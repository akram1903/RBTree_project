import traceback


class RBNode:
    value = 0
    right = None
    left = None
    parent = None
    black = 0

    def __init__(self, value, parent):
        self.value = value
        self.parent = parent

    def get_grand_parent(self):
        if self.parent is None:
            pass
        if self.parent.parent is None:
            pass
        else:
            return self.parent.parent

    def get_uncle(self):
        if self.parent is None:
            pass
        if self.parent.parent is None:
            pass
        elif self.value < self.parent.value:
            return self.parent.parent.right
        else:
            return self.parent.parent.left

    def isRoot(self):
        if self.parent is None:
            return True
        else:
            return False
    def isBlack(self):
        if self.black == 0:
            return False
        else:
            return True

    def isDoubleBlack(self):
        if self.black == 2:
            return True
        else:
            return False

    def changeColor(self):
        if self.black == 0:
            self.black = 1
        elif self.black == 1:
            self.black = 0
        else:
            print("can't recolor double black node")

    def __str__(self):
        if self.isDoubleBlack():
            return f"{self.value} , Double Black"
        elif self.isBlack():
            return f"{self.value} , Black"
        else:
            return f"{self.value} , Red"

    def isRight(self):
        if self.parent is None:
            return True
        if self.parent.right is not None:
            if self.parent.right.value == self.value:
                return True
        else:
            return False

    def isLeft(self):
        if self.parent is None:
            return True
        if self.parent.left is not None:
            if self.parent.left.value == self.value:
                return True
        else:
            return False

    def isInline(self):
        # if self.parent is None:
        #     return True
        if self.isRight and self.parent.isRight:
            return True
        elif self.isLeft and self.parent.isLeft:
            return True
        else:
            print("Error :(")
            return traceback

    def isLeaf(self):
        if self.right is None and self.left is None:
            return True
        return False
