class MyStack:
    def __init__(self, size):
        self.size = size
        self.arr = [-1] * size
        self.top = -1

    def is_empty(self):
        if self.top == -1:
            return True

        else:
            return False
        
    def push(self, val):
        if self.top == self.size-1:
            return None
        self.top += 1
        self.arr[self.top]=val

    def pop(self):
        if self.is_empty():
            return None
        e = self.arr[self.top]
        self.arr[self.top]=-1
        self.top -= 1

        return e
    
    def to_string(self):
        stringfied_data = "["
        for i in range(0,self.top+1):
            stringfied_data+=str(self.arr[i]) + " "
        return stringfied_data +"]"    
if __name__ == "__main__":
    my_stack = MyStack(6)
    my_stack.push(6)
    my_stack.push(2)
    my_stack.push(3)
    my_stack.push(7)
    my_stack.push(9)
    print('top = ', my_stack.top)
    print('初期値: ', my_stack.to_string())

    x = my_stack.pop()
    y = my_stack.pop()

    if x != None and y != None:
        print("取り出した要素: ", x, y)
        print('top = ', my_stack.top)
        print('初期値: ', my_stack.to_string())

        my_stack.push(5)
        my_stack.push(8)
        print('top = ', my_stack.top)
        print('初期値: ', my_stack.to_string())

        



