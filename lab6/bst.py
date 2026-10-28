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

    def parenthesis(self):

        if self.root is None:
            return "()"
        else:
            return "(" + str(self.root.data) + " " + self.root.string() + ")"



if __name__ == '__main__':

    bst = BST()
    bst1 = BST()

    bst.add(11)
    bst.add(2)
    bst.add(1)
    bst.add(3)
    bst.add(4)
    bst.add(5)
    bst.add(6)
    bst.add(20)
    bst.add(25)
    bst.add(13)

    bst1.add(11)
    bst1.add(7)
    bst1.add(13)

    
    balan = BST()

    balan.add(11)
    balan.add(7)
    balan.add(5)
    balan.add(3)
    balan.add(9)
    balan.add(8)
    balan.add(10)
    balan.add(15)
    balan.add(13)
    balan.add(16)

    
    print('BST 1')
    print(bst)
    print('Paranthetical String: ', bst.parenthesis())
    print('Contains: should be True: ', (25 in bst))
    print('Contains: should be False: ', (0 in bst))
    print('Height: ', bst.height())
    print('Length: ', len(bst))
    print('Balance: should be False: ', bst.isBalanced())

    print()
    print('BST 2')
    print(bst1)
    print('Paranthetical String: ', bst1.parenthesis())
    print('Contains: should be True: ', (7 in bst1))
    print('Contains: should be False: ', (2 in bst1))
    print('Height: ', bst1.height())
    print('Length: ', len(bst1))
    print('Balance: should be True: ', bst1.isBalanced())

    print()
    print(balan)
    print('Paranthetical String: ', balan.parenthesis())
    print('Contains: should be True: ', (16 in balan))
    print('Contains: should be False: ', (2 in balan))
    print('Height: ', balan.height())
    print('Length: ', len(balan))
    print('Balance: should be True: ', balan.isBalanced())
    
