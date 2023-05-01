class MyQueue:
    def __init__(self, size):
        self.size = size
        self.arr = [-1] * size
        self.head = 0
        self.tail = 0
    
    def enqueue(self,val):
        if (self.tail +1) % self.size == self.head:
            return None
        
        self.arr[self.tail] = val

        self.tail = (self.tail +1) % self.size

    def dequeue(self):
        if self.head == self.tail:
            return None
        e = self.arr[self.head]
        self.arr[self.head]=-1
        self.head = (self.head + 1) % self.size

        return e