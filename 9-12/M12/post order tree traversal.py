# Python program for postorder traversals

# Structure of a Binary Tree Node

class Node:
    def __init__(self, key):        
        self.left = None
        self.right = None
        self.val = key

# Function to print postorder traversal


def printPostorder(node):
    if node == None:
        return

    # First recur on left subtree
    printPostorder(node.left)

    # Then recur on right subtree
    printPostorder(node.right)

    # Now deal with the node
    print(node.val, end=' ')


# Driver code
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.right = Node(6)

# Function call
print("Postorder traversal of binary tree is:")
printPostorder(root)