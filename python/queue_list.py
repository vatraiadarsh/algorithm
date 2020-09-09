class ListQueue(object):
    def __init__(self):
        self.items = []
        self.size = 0

    def empty(self):
        return self.items == []

    """The enqueue operation adds an item to the queue.
        => It uses the insert method of the list class to insert items (or data) at the front of the list. 
        => The array index 0 is the only place where new data elements are inserted into the queue. 
        The insert operation will shift existing data elements in the list by one position up and then 
        insert the new data in the space created at index 0
        
        We could have used Python's shift method on the list as another way of implementing the insert at 0. 
    """

    def enqueue(self, data):
        self.items.insert(0, data)  # Always insert items at index 0
        self.size += 1  # increment the size of the queue by 1

    """The dequeue operation deletes an item from the queue.
       This method returns the topmost item from the queue and deletes it from the queue. 
    """

    def dequeue(self):
        data = self.items.pop()
        self.size -= 1
        return data

    def size1(self):
        return self.size


q = ListQueue()
q.enqueue(4)
q.enqueue('dog')
q.enqueue('True')

a1 = q.size1()
print(a1)

print("After dequeing the size is {}".format(q.size1()))
