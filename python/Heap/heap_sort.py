class Heap:
    def __init__(self):
        self.heap = [0]
        self.size = 0

    def float(self, k):
        while k // 2 > 0:
            if self.heap[k] < self.heap[k//2]:
                self.heap[k], self.heap[k//2] = self.heap[k//2], self.heap[k]
            k //= 2

    def insert(self, item):
        self.heap.append(item)
        self.size += 1
        self.float(self.size)

    def sink(self, k):
        while k * 2 <= self.size:
            mc = self.minchild(k)
            if self.heap[k] > self.heap[mc]:
                self.heap[k], self.heap[mc] = self.heap[mc], self.heap[k]
            k = mc

    def minchild(self, k):
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

    def heap_sort(self):
        sorted_list = []
        for node in range(self.size):
            n = self.pop()
            sorted_list.append(n)

        return sorted_list


h = Heap()

unsorted_list = [-2, 45, 0, 11, -9]
for i in unsorted_list:
    h.insert(i)
print("Unsorted list: {}".format(unsorted_list))
sorted_list = h.heap_sort()
print("Sorted list: {}".format(sorted_list))

print("**********************************************************************")

unsorted_list = ['abpple', 'aapple', 'len', 'mon', 'tues', 'cat', 'car']
for i in unsorted_list:
    h.insert(i)
print("Unsorted list: {}".format(unsorted_list))
sorted_list = h.heap_sort()
print("Sorted list: {}".format(sorted_list))
