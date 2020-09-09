class Node(object):
    def __init__(self, data=None):
        self.data = data

    """
    We will need two things to implement a stack using nodes:
        We first need to know the node which is at the top of the stack so that we will be able to apply 
        the push and pop operations through this node.
        
        We would also like to keep track of the number of nodes in the stack, 
        so we add a size variable to the stack class.
    """


class Stack(object):
    def __init__(self):
        self.top = None
        self.size = 0

    """
    Push Operation we have to do two things:
        1)The new node must have its next pointer pointing to the node that was at the top earlier
        2)we put the new node at the top of the stack pointing self.top to the newly added node
        
    """

    def push(self, data):
        node = Node(data)
        if self.top:
            node.next = self.top
            self.top = node
        else:
            self.top = node
        self.size += 1

    """
    Pop Operation we have to do following things:
        1)First, check if the stack is empty. The pop operation is not allowed on an empty stack.
        
        2)If the stack is not empty, it can be checked if the top node has its next attribute pointing to some other node. 
        It means the stack has elements, and the topmost node is pointing to the next node in the stack. 
        To apply the pop operation, we have to change the top pointer. The next node should be at the top. 
        We do this by pointing self.top to self.top.next
        
        3)When there is only one node in the stack, the stack will be empty after the pop operation.
         We have to change the top pointer to None
        4)We also decrement the size of the stack by 1 if the stack is not empty.
    """

    def pop(self):
        if self.top:
            data = self.top.data
            self.size -= 1
            if self.top.next:
                self.top = self.top.next
            else:
                self.top = None
            return data
        else:
            return None

    def peek(self):
        if self.top:
            return self.top.data
        else:
            return None
