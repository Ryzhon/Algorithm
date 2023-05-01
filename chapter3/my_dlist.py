class MyElement:
    def __init__(self, val):
        self.val = val
        self.prev =None
        self.next = None

    def to_string(self):
        str_prev = "None"
        str_next = "None"

        if self.prev != None:
            str_prev = str(self.prev.val)
        if self.next != None:
            str_next - str(self.next.val)
        
        return 
    
class MyDoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, element):
        if self.head ==None:
            self.head = element
            self.tail = element
        else:
            self.tail.next = element
            element.prev = self.tail
            self.tail = element

    def get(self,index):
        ptr = self.head
        for i in range(0,index):
            ptr = ptr.next

        return ptr
    
    def insert(self,index,element):
        ptr = self.get(index)

        if ptr == None:
            self.append(element)
        else:
            #element.prev = ptr.prev
            #と
            # if ptr.prev == None:
            #   self.head = element
            #逆の方がいいのでは？
            
            element.prev = ptr.prev
            element.next = ptr
            if ptr.prev == None:
                self.head = element
            else:
                #ここ理解不能ptrの前を指しているポインタの次のポインタって自分やないかい
                ptr.prev.next = element
            ptr.prev = element

    def delete(self, element):
        if element.prev == None:
            self.head = element.next
        else:
            element.prev.next = element.next

        if element.next == None:
            self.tail = element.prev
        else:
            element.next.prev = element.prev

    def to_string(self):
        stringfied_data = "["
        ptr = self.head
        while ptr != None:
            stringfied_data += str(ptr.val) +" "
            ptr = ptr.next
        return stringfied_data + "]"
    
if __name__ == "__main__":
    my_list = MyDoublyLinkedList()

    my_list.append(MyElement(6))
    my_list.append(MyElement(2))
    my_list.append(MyElement(3))
    my_list.append(MyElement(7))
    my_list.append(MyElement(9))

    print("初期値: ", my_list.to_string())
    


