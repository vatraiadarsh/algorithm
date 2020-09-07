class Node(object):
    """ A singly-linked node. """

    def __init__(self, data=None):
        self.data = data
        self.next = None


class SinglyLinkedList(object):
    """ A singly-linked list. """

    def __init__(self):
        """ Create an empty list """
        self.head = None  # reference to the first node in the list
        self.tail = None  # reference to the last node in the list
        self.count = 0

    """
    We encapsulate data in a node so that it has the next pointer attribute.
    From here, we check if there are any existing nodes in the list
    (that is, whether self.tail points to a Node or not).
    
    If there is None, we make the new node the first node of the list; 
    otherwise, we find the insertion point by traversing the list to the last node, 
    updating the next pointer of the last node to the new node.
    """

    def append(self, data):
        node = Node(data)  # Encapsulate the data in a Node
        if self.head:
            self.head.next = node
            self.head = node
        else:
            self.tail = node
            self.head = node
        self.count += 1

    def iter(self):
        """ Iterate through the list. """
        current = self.tail
        while current:
            val = current.data
            current = current.next
            yield val

    def delete(self, data):
        """ Delete a node from the list """
        current = self.tail
        prev = self.tail
        while current:
            if current.data == data:
                if current == self.tail:
                    self.tail = current.next
                else:
                    prev.next = current.next
                self.count -= 1
                return
            prev = current
            current = current.next

    def search(self, data):
        """ Search through the list. Return True if data is found, otherwise
        False. """
        for node in self.iter():
            if data == node:
                return True
        return False

    def clear(self):
        """ Clear the entire list. """
    self.tail = None
    self.head = None


words = SinglyLinkedList()
words.append('foo')
words.append('bar')
words.append('bim')
words.append('baz')
words.append('quux')


print("This list has {} elements.".format(words.count))
for word in words.iter():
    print("Got this data: {}".format(word))

if words.search('foo'):
    print("Found foo in the list.")
if words.search('amiga'):
    print("Found amiga in the list.")

print("Now we try to delete an item")
words.delete('bim')
print("List now has {} elements".format(words.count))
for word in words.iter():
    print("data: {}".format(word))

print("delete the first item in the list")
words.delete('foo')
print("size: {}".format(words.count))
for word in words.iter():
    print("data: {}".format(word))

print("delete the last item in the list")
words.delete('quux')
print("size: {}".format(words.count))
for word in words.iter():
    print("data: {}".format(word))
