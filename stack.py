class Stack:
    def __init__(self):
        self.items = []
        
    def push(self, item):
        self.items.append(item)
        
    def pop(self):
        return self.items.pop()
    
    def is_empty(self):
        return self.items == []
    
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
    
    def size(self):
        return len(self.items)
    
    def get_stack(self):
        return self.items
    
    
stack = Stack()
print(stack.is_empty())
stack.push("A")
stack.push("B")
print(stack.get_stack())
stack.push("C")
print(stack.is_empty())
print(stack.get_stack())
print(stack.pop())
print(stack.get_stack())
print(stack.peek())
print(stack.size())


