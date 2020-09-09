"""
Breadth-first traversal
   Breadth-first traversal starts from the root of the tree and then visits 
   every node on the next level of the tree. Then, we move to the next level in the tree, 
   and so on. This kind of tree traversal is breadth-first as it broadens the tree by traversing 
   all the nodes in a level before going deep into the tree. 

      
"""
from collections import deque


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


def breadth_first_traversal(root_node):
    list_of_nodes = []
    traversal_queue = deque([root_node])
    # We enqueue the root node[self.root_node] and keep a list of the visited nodes in the list_of_nodes list.
    #  The dequeue class is used to maintain a queue:

    while len(traversal_queue) > 0:
        node = traversal_queue.popleft()
        list_of_nodes.append(node.data)
        if node.left_child:
            traversal_queue.append(node.left_child)
        if node.right_child:
            traversal_queue.append(node.right_child)
    return list_of_nodes

    """
    If the number of elements in traversal_queue is greater than zero, the body of the loop is executed.
    The node at the front of the queue is popped off and appended to the list_of_nodes list. The first if 
    statement will enqueue the left child node if the node provided with a left node exists. The second if 
    statement does the same for the right child node. and
    the list_of_nodes list is returned in the last statement.
    """


print(breadth_first_traversal(n1))
