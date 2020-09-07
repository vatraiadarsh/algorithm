"""
To create a doubly liked list Node includes it's initializing methods
the prev pointer, the next pointer && data instance variable

"""


class Node(object):
    """ A Doubly-linked lists' node. """

    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev


class DoublyLinkedList(object):
    def __init__(self):
        self.head = None  # points to the beginner node of the list
        self.tail = None  # points to the latest node added to the list
        self.count = 0

    """
    If the new node is to be added to a list, the new node's previous variable is to be set to the tail of the list:
        new_node.prev = self.tail
    The tail's next pointer (or variable) has to be set to the new node:
        self.tail.next = new_node
    Lastly, we update the tail pointer to point to the new node:
        self.tail = new_node
    """

    def append(self, data):
        """ Append an item to the list. """

        new_node = Node(data, None, None)
        if self.head is None:
            self.head = new_node
            self.tail = self.head
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

        self.count += 1

    def iter(self):
        """ Iterate through the list. """
        current = self.head  # note subtle change
        while current:
            val = current.data
            current = current.next
            yield val

    def reverse_iter(self):
        """ Iterate backwards through the list. """
        current = self.tail
        while current:
            val = current.data
            current = current.prev
            yield val

    """
    The delete operation in a doubly linked list can encounter the following four scenarios:
        The search item to be deleted is not found in the list
        The search item to be deleted is located in the middle of the list
        The search item to be deleted is located at the start of the list
        The search item to be deleted is found at the tail end of the list
    """

    def delete(self, data):
        """ Delete a node from the list. """
        current = self.head
        node_deleted = False
        if current is None:  # Item to be deleted is not found in the list
            node_deleted = False

        elif current.data == data:  # Item to be deleted is found at starting of list
            self.head = current.next
            self.head.prev = None
            node_deleted = True

        elif self.tail.data == data:   # Item to be deleted is found at the end of list
            self.tail = self.tail.prev
            self.tail.next = None
            node_deleted = True

        else:    # search item to be deleted, and delete that node
            while current:
                if current.data == data:
                    current.prev.next = current.next
                    current.next.prev = current.prev
                    node_deleted = True
                current = current.next

        if node_deleted:
            self.count -= 1

    """[A]      [B]        [C]
                To delete node B in the middle of the list,
                we will essentially make A point to node C as its next node,
                while making C point to A as its previous node:

                we search for the node to be deleted by looping through the whole list of the nodes.
                If the data that is to be deleted is matched with a node, that node will be deleted.
                To delete a node, we make the previous node of the current node to point to the current's next node using the code
                    current.prev.next = current.next.
                After that step, we make the current's next node to point to the previous node of the current node using
                    current.next.prev = current.prev.
    """

    def search(self, data):
        """Search through the list. Return True if data is found, otherwise False."""
        for node in self.iter():
            if data == node:
                return True
        return False

    def print_foward(self):
        """ Print nodes in list from first node inserted to the last . """
        for node in self.iter():
            print(node)

    def print_backward(self):
        """ Print nodes in list from latest to first node. """
        current = self.tail
        while current:
            print(current.prev)
            current = current.prev

    def insert_head(self, data):
        """ Insert new node at the head of linked list. """

        if self.head is not None:
            new_node = Node(data, None, None)
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
            self.count += 1

    def reverse(self):
        """ Reverse linked list. """
        current = self.head
        while current:
            temp = current.next
            current.next = current.prev
            current.prev = temp
            current = current.prev

        # Now reverse the order of head and tail
        temp = self.head
        self.head = self.tail
        self.tail = temp


dll = DoublyLinkedList()
dll.append("foo")
dll.append("bar")
dll.append("biz")
dll.append("whew")
print("Items in List : ")
dll.print_foward()
print("List after deleting node with data whew")
dll.delete("whew")

print("List count: {}".format(dll.count))


print("Reverse list ")
dll.reverse()
dll.print_foward()

print("Append item to front of list")
dll.insert_head(55)
dll.print_foward()
