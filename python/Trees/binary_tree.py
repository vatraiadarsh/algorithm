class Node:
    def __init__(self, data):
        self.data = data
        self.right_child = None
        self.left_child = None


class Tree:
    def __init__(self):
        self.root_node = None

    def find_min(self):
        current = self.root_node
        while current.left_child:
            current = current.left_child

        return current
    # The while loop continues to get the left node and visits it until the last left node points to None

    def find_max(self):
        current = self.root_node
        while current.right_child:
            current = current.right_child

        return current

    def insert(self, data):
        node = Node(data)
        if self.root_node is None:
            self.root_node = node
        else:
            current = self.root_node
            parent = None
            while True:
                parent = current
                if node.data < parent.data:
                    current = current.left_child
                    if current is None:
                        parent.left_child = node
                        return
                else:
                    current = current.right_child
                    if current is None:
                        parent.right_child = node
                        return
    """
    we encapsulate the data in a node. This way, we hide away the node class from the client code, 
    who only needs to deal with the tree:
    
    
    A first check will be done to find out whether we have a root node. 
    If we don't, the new node becomes the root node (we cannot have a tree without a root node):
    
    As we walk down the tree, we need to keep track of the current node we are working on, as well as its parent. 
    The current variable is always used for this purpose:
                current = self.root_node 
                parent = None 
                while True: 
                    parent = current 
                    
    
    Here, we must perform a comparison. If the data held in the new node is less than the data held in the current node, 
    then we check whether the current node has a left child node. If it doesn't, this is where we insert the new node. 
    Otherwise, we keep traversing
    
            if node.data < current.data: 
            current = current.left_child 
            if current is None: 
                parent.left_child = node 
                return 
    
    Now, we need to take care of the greater than or equal case. 
    If the current node doesn't have a right child node, then the new node is inserted as the right child node. 
    Otherwise, we move down and continue looking for an insertion point:
    
            else: 
            current = current.right_child 
            if current is None: 
                parent.right_child = node 
                return 
                
        Insertion of a node in a BST takes O(h), where h is the height of the tree.
    
    """

    def get_node_with_parent(self, data):
        parent = None
        current = self.root_node
        if current is None:
            return (parent, None)
        while True:
            if current.data == data:
                return (parent, current)
            elif current.data > data:
                parent = current
                current = current.left_child
            else:
                parent = current
                current = current.right_child

        return (parent, current)

        """
        For the deletion there are 3 cases
        -> No children: If there is no leaf node, directly remove the node
        -> One child: In this case, we swap the value of that node with its child, and then delete the node
        -> Two children: In this case, we first find the in-order successor or predecessor, 
            swap the value with it, and then delete that node
        
        """

    def remove(self, data):
        parent, node = self.get_node_with_parent(data)

        if parent is None and node is None:
            return False

        # Get Children count

        children_count = 0
        if node.left_child and node.right_child:
            children_count = 2
        elif (node.left_child is None) and (node.right_child is None):
            children_count = 0
        else:
            children_count = 1

        # We pass the parent and the found nodes to parent and node,
        # respectively with the parent, node = self.get_node_with_parent(data) line.
        # It is important to know the number of children that the node has that we want to delete,
        #  and we do so in the if statement.
        # After we know the number of children a node has that we want to delete,
        # we need to handle various conditions in which a node can be deleted.
        # The first part of the if statement handles the case where the node has no children:

        if children_count == 0:
            if parent:
                if parent.right_child is node:
                    parent.right_child = None
                else:
                    parent.left_child = None
            else:
                self.root_node = None

            # In cases where the node to be deleted has only one child, theelifpart of the if statement does the following
        elif children_count == 1:
            next_node = None
            if node.left_child:
                next_node = node.left_child
            else:
                next_node = node.right_child

            if parent:
                if parent.left_child is node:
                    parent.left_child = next_node
                else:
                    parent.right_child = next_node
            else:
                self.root_node = next_node

            # The next_node is used to keep track of that single node. which is the child of the node that is to be deleted.
            #  We then connect parent.left_child or parent.right_child to next_node

        else:
            parent_of_leftmost_node = node
            leftmost_node = node.right_child
            while leftmost_node.left_child:
                parent_of_leftmost_node = leftmost_node
                leftmost_node = leftmost_node.left_child

            node.data = leftmost_node.data

    def search(self, data):
        current = self.root_node
        while True:
            if current is None:
                return None
            elif current.data is data:
                return data
            elif current.data > data:
                current = current.left_child
            else:
                current = current.right_child


tree = Tree()
tree.insert(5)
tree.insert(2)
tree.insert(7)
tree.insert(9)
tree.insert(1)

for i in range(1, 10):
    found = tree.search(i)
    print("{}: {}".format(i, found))

print("\r\n\t----------------------")
tree.remove(7)
tree.remove(5)
tree.remove(2)

for i in range(1, 10):
    found = tree.search(i)
    print("{}: {}".format(i, found))
