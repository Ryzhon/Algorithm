import my_dlist

class MyQueue:
    def __init__(self):
        self.dlist = my_dlist.MyDoublyLinkedList()

    def enqueue(self, element):
        self.dlist.append(element)

    def dequeue(self):
        e = self.dlist.get(0)
        self.dlist.delete(e)

        return e
    
    def to_string(self):
        return self.dlist.to_string()