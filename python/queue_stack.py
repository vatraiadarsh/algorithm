"""Impl of queue using 2 stack
"""


class Queue:
    def __init__(self):
        self.inbound_stack = []
        # Theinbound_stack is only used to store elements that are added to the queue.
        #  No other operation can be performed on this stack.
        self.outbound_stack = []

    def enqueue(self, data):
        self.inbound_stack.append(data)
        # the append method is used to mimic the push operation, which pushes elements to the top of the stack.

    """New elements added to our queue end up in the inbound_stack. 
    Instead of removing elements from the inbound_stack, we shift our attention to another stack, that is, outbound_stack. 
    We shall delete the elements from our queue only through the outbound_stack.   
    
    
    We first check if the outbound_stack is empty or not. 
    
        As it is empty at the start, we move all the elements of the inbound_stack to the outbound_stack using the pop operation on the stack. 
        Now the inbound_stack becomes empty and the outbound_stack keeps the elements. 
        
        Now, if the outbound_stack is not empty, we proceed to remove the items from the queue using the pop operation.
    """

    def dequeue(self):
        if not self.outbound_stack:
            while self.inbound_stack:
                self.outbound_stack.append(self.inbound_stack.pop())
            return self.outbound_stack.pop()

    """
    The if statement first checks whether the outbound_stack is empty or not. 
    If it is not empty, we proceed to remove the element at the front of the queue using the pop method, shown as follows:
        return self.outbound_stack.pop() 
        
    If the outbound_stack is empty instead, all the elements in the inbound­_stack are moved to the outbound_stack
    before the front element in the queue is popped out:
        while self.inbound_stack: 
            self.outbound_stack.append(self.inbound_stack.pop()) 
            
    The while loop will continue to be executed as long as there are elements in the inbound_stack
        The self.inbound_stack.pop() statement will remove the latest element that was added to the 
        inbound_stack and immediately passes the popped data to the self.outbound_stack.append() method call.
    """


queue = Queue()
queue.enqueue(5)
queue.enqueue(6)
queue.enqueue(7)
print(queue.inbound_stack)

queue.dequeue()
print(queue.inbound_stack)

print(queue.outbound_stack)
queue.dequeue()
print(queue.outbound_stack)
