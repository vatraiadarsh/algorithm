import time
from random import randint


class Node(object):
    """ A Doubly-linked lists' node. """

    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev


class Queue(object):
    """ A doubly-linked list. """

    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

        """
        The enqueue method code is very similar to the append operation of the doubly linked list 
        
        The enqueue operation creates a node from the data passed to it and appends it to the tail of the queue, 
        and points both self.head and self.tail to the newly created node if the queue is empty. 
        The total count of elements in the queue is increased by the line self.count += 1. 
        If the queue is not empty, the new node's previous variable is set to the tail of the list, 
        and the tail's next pointer (or variable) is set to the new node. 
        Lastly, we update the tail pointer to point to the new node.     
        """

    def enqueue(self, data):
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

        """
        The other operation that makes our doubly linked list behave as a queue is the dequeue method. 
        This method removes the node at the front of the queue. 
        To remove the first element pointed to by self.head, an if statement is used:
        
        current is initialized by pointing it to self.head. 
        If self.count is 1, then it means only one node is in the list and invariably the queue.
        Thus, to remove the associated node (pointed to by self.head), the self.head and self.tail variables are set to None.
        
        If the queue has many nodes, then the head pointer is shifted to point to the next node after self.head.
        
        """

    def dequeue(self):
        """ Remove elements from the front of the list"""
        current = self.head
        if self.count == 1:
            self.count -= 1
            self.head = None
            self.tail = None
        elif self.count > 1:
            self.head = self.head.next
            self.head.prev = None
            self.count -= 1
        return current

        # we have implemented a queue, borrowing heavily from the idea of a doubly linked list.


queue = Queue()

start_time = time.time()
for i in range(100000):
    queue.enqueue(i)
for i in range(100000):
    queue.dequeue()
print("--- %s seconds ---" % (time.time() - start_time))


# Media player queues Impl


class Track:
    # Each track holds a reference to the title of the song and also the length of the song.
    # The length of the song is a random number between 5 and 10
    def __init__(self, title=None):
        self.title = title
        self.length = randint(5, 10)


class MediaPlayerQueue(Queue):

    def __init__(self):
        super(MediaPlayerQueue, self).__init__()

    def add_track(self, track):
        self.enqueue(track)

    def play(self):
        while self.count > 0:
            current_track_node = self.dequeue()
            print("Now Playing {}".format(current_track_node.data.title))
            time.sleep(current_track_node.data.length)


track1 = Track("white whistle")
track2 = Track("butter butter")
track3 = Track("Oh black star")
track4 = Track("Watch that chicken")
track5 = Track("Don't go")
track6 = Track("Never Really Over")
track7 = Track("Smile")
media_player = MediaPlayerQueue()
media_player.add_track(track1)
media_player.add_track(track2)
media_player.add_track(track3)
media_player.add_track(track4)
media_player.add_track(track5)
media_player.add_track(track6)
media_player.add_track(track7)
media_player.play()
