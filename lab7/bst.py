import math

class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add(self, node):

        if node.data < self.data:
            if self.left is None:
                self.left = node
            else:
                self.left.add(node)

        else:
            if self.right is None:
                self.right = node
            else:
                self.right.add(node)

    def search(self, data):

        if data < self.data:
            if self.left is None:
                return False
            else:
                return self.left.search(data)

        elif data > self.data:
            if self.right is None:
                return False
            else:
                return self.right.search(data)

        else:
            return True

    def get_height(self):

        if self.left:
            leftH = 1 + self.left.get_height()
        else:
            leftH = 0
        if self.right:
            rightH = 1 + self.right.get_height()
        else:
            rightH = 0

        return max(leftH, rightH)

    def get_len(self):
        if self.left:
            leftH = 1 + self.left.get_len()
        else:
            leftH = 0
        if self.right:
            rightH = 1 + self.right.get_len()
        else:
            rightH = 0

        return (leftH + rightH)

    def string(self):
        if self.left:
            left = "(" + str(self.left.data) + " " + str(self.left.string()) + ")"
        else:
            left = "_" + " "
        if self.right:
            right = "(" + str(self.right.data) + " " + str(self.right.string()) + ")"
        else:
            right = "_"

        return left + right
            

class BST:

    def __init__(self):

        self.root = None

    def add(self, data):

        node = Node(data)

        if self.root is None:

            self.root = node

        else:

            self.root.add(node)      

    def __contains__(self, data):

        if self.root is None:
            return False
        else:
            return self.root.search(data)

    def __str__(self):
        
        def recurse(node, level):
            s = ""
            if node != None:
                s += recurse(node.right, level + 1)
                s += "| " * level
                s += str(node.data) + "\n"
                s += recurse(node.left, level + 1)
            return s
    
        return recurse(self.root, 0)

    def height(self):
        #return number of steps from the root to the deepest leaf
        if self.root is None:
            return 0
        else:
            return self.root.get_height()

    def __len__(self):
        if self.root is None:
            return 0
        else:
            return 1 + self.root.get_len()

    def isBalanced(self):

        h = self.height()
        l = len(self)

        if h <= math.ceil(math.log2(l)):
            return True

        return False

    def para(self):

        if self.root is None:
            return "()"
        else:
            return "(" + str(self.root.data) + " " + self.root.string() + ")"


    def preorder(self):
        """Supports a preorder traversal on a view of self."""
        lyst = list()
    
        def recurse(node):
            if node != None:
                lyst.append(node.data)
                recurse(node.left)
                recurse(node.right)
    
        recurse(self.root)
    
        return lyst

    def postorder(self):
        """Supports a postorder traversal on a view of self."""
        lyst = list()
    
        def recurse(node):
            if node != None:
                recurse(node.left)
                recurse(node.right)
                lyst.append(node.data)
    
        recurse(self.root)
    
        return lyst

    def inorder(self):
        """Supports a postorder traversal on a view of self."""
        lyst = list()
    
        def recurse(node):
            if node != None:
                recurse(node.left)
                lyst.append(node.data)
                recurse(node.right)
    
        recurse(self.root)
    
        return lyst

    def balanced(self):
        order = self.inorder()
        new = BST()

        def recurse(left, right):  # indexes into the list
           if left <= right:
               midpoint = (right+left)//2
               new.add(order[midpoint])
               recurse(left, midpoint - 1)
               recurse(midpoint + 1, right)

        recurse(0, len(order)-1)

        return new



if __name__ == '__main__':

    bst = BST()

    bst.add(11)
    bst.add(7)
    bst.add(2)
    bst.add(9)
    bst.add(15)
    bst.add(13)
    bst.add(19)

    print("preorder: ", bst.preorder())
    print("inorder: ", bst.inorder())
    print("postorder: ", bst.postorder())
    print(bst.balanced())

    unbalanced = BST()
    unbalanced.add(8)
    unbalanced.add(7)
    unbalanced.add(6)
    unbalanced.add(5)
    unbalanced.add(4)
    unbalanced.add(3)
    unbalanced.add(2)

    print("Unbalanced preorder: ", unbalanced.preorder())
    print("Unbalanced inorder: ", unbalanced.inorder())
    print("Unbalanced postorder: ", unbalanced.postorder())
    print(unbalanced)
    print("Unbalanced tree now balanced:")
    print(unbalanced.balanced())
