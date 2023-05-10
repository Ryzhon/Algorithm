class MyElement:
    def __init__(self, val):
        self.val = val
        self.next = None
    
class MyStack:
    def __init__(self):
        if self.top == None:
            return True
        else:
            return False
        
    def push(self, element):
        if self.top != None:
            element.next = self.top
        self.top = element

    def pop(self):
        if self.is_empty():
            return None
        e = self.top
        self.top = e.next
        e.next = None

        return e
    
    def to_string(self):
        stringfied_data = "[ "
        ptr = self.top
        while ptr != None:
            stringfied_data += str(ptr.val) + " "
            ptr = ptr.next

        return stringfied_data + "]"
