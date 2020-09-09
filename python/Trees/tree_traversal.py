

class Node:
    def __init__(self, data):
        self.data = data
        self.right_child = None
        self.left_child = None


n1 = Node("root node")
n2 = Node("left child node")
n3 = Node("right child node")
n4 = Node("left grandchild node")
n1.left_child = n2
n1.right_child = n3
n2.left_child = n4

current = n1
while current:
    print(current.data)
    current = current.left_child

"""
The method to visit all the nodes in a tree is called tree traversal.
This can be done either depth-first search (DFS) or breadth-first search (BFS).


Depth-first traversal
    In depth-first traversal, we traverse the tree,
    starting from the root, and go deeper into the tree as much as possible on each child,
    and then continue to traverse to the next sibling. We use the recursive approach for tree traversal.

        3 Forms
                =>In-order traversal
                    ->We start traversing the left sub-tree and call the inorder function recursively
                    ->Next, we visit the root node
                    ->Finally, we traverse the right sub-tree and call the inorder function recursively

                =>Pre-order traversal
                    ->We start traversing with the root node
                    ->Next, we traverse the left sub-tree and call the preorder function with the left sub-tree recursively
                    ->Next, we visit the right sub-tree and call the preorder function with the right sub-tree recursively
                =>Post-order traversal
                    ->We start traversing the left sub-tree and call the postorder function recursively
                    ->Next, we traverse the right sub-tree and call the postorder function recursively
                    ->Finally, we visit the root node

"""

print("\n\r\t==========================")


def inorder(root_node):
    current = root_node
    if current is None:
        return
    inorder(current.left_child)
    print(current.data)
    inorder(current.right_child)

    """
    We visit the node by printing the visited node.
    In this case, we first recursively call the inorder function with current.left_child,
    then we visit the root node, and finally we recursively call the inorder function with current.right_child once more.
    """


def preorder(root_node):
    current = root_node
    if current is None:
        return
    print(current.data)
    preorder(current.left_child)
    preorder(current.right_child)


def postorder(root_node):
    current = root_node
    if current is None:
        return
    postorder(current.left_child)
    postorder(current.right_child)
    print(current.data)


inorder(n1)
print("\n")
preorder(n1)
print("\n")
postorder(n1)
