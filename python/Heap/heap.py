class Heap:
    def __init__(self):
        self.heap = [0]
        self.size = 0

        # Insertion Operation

        """We can retrieve the children of any node at the n index very easily. 
        =:The left child is located at 2n, and the right child is located at 2n + 1. This will always hold true. 
        
        Inserting an item to the min heap works in two steps.
        =: First, we add the new element to the end of the list (which we understand to be the bottom of the tree), 
            and we increment the size of the heap by one.
        =:  Secondly, after each insertion operation, we need to arrange the new element up in the heap tree,
            to organize all the nodes in such a way that it satisfies the heap property. 
            This is to remind us that the lowest element in the min-heap needs to be the root element. 
            
        =: We first create a helper method, called arrange, that takes care of arranging all the nodes after insertion.
        """

    def arrange(self, k):
        while k // 2 > 0:
            if self.heap[k] < self.heap[k//2]:
                self.heap[k], self.heap[k//2] = self.heap[k//2], self.heap[k]
            k //= 2

        """while k//2 >0 
        we are going to loop untill we have reached the root node, 
        so we can keep arranging the element up as high as it need to go
        Since we are using integer division, as soon as we get below 2, the loop will break out:
        
        Compare between the parent and child. If the parent is greater than the child, swap the two values:
            if self.heap[k] < self.heap[k//2]: 
            self.heap[k], self.heap[k//2] = self.heap[k//2], 
            self.heap[k] 
        
        Finally, moving up the tree:
        """

    def insert(self, item):
        self.heap.append(item)
        self.size += 1
        self.arrange(self.size)

    def sink(self, k):
        while k * 2 <= self.size:
            mi = self.miniindex(k)
            if self.heap[k] > self.heap[mi]:
                self.heap[k], self.heap[mi] = self.heap[mi], self.heap[k]
            k = mi

    def miniindex(self, k):
        if k * 2 + 1 > self.size:
            return k * 2
        elif self.heap[k*2] < self.heap[k*2+1]:
            return k * 2
        else:
            return k * 2 + 1

    def pop(self):
        item = self.heap[1]
        self.heap[1] = self.heap[self.size]
        self.size -= 1
        self.heap.pop()
        self.sink(1)
        return item


h = Heap()
for i in (4, 8, 7, 2, 9, 10, 5, 1, 3, 6):
    h.insert(i)
print(h.heap)

print("\n=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:\n")

for i in range(10):
    n = h.pop()
    print(n)
    print(h.heap)
