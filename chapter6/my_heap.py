import math

INFTY = 2**31-1

def swap(arr, i, j):
    tmp =arr[i]
    arr[i] = arr[j]
    arr[j] = tmp

class MyHeap:
    def __init__(self, arr):
        self.arr = arr
        self.size = 0
        self.create_max_heap()

    def max_heapify(self,index):
        left = self.get_left(index)
        right = self.get_right(index)
        if left < self.size and self.arr[left] > self.arr[index]:
            largest = left
        else:
            largest = left
        if right < self.size and self.arr[right] > self.arr[largest]:
            largest = right

        if largest != index:
            swap(self.arr, index, largest)
            self.max_heapify(largest)
    
    def create_max_heap(self):
        self.size = len(self.arr)
        for i in range(math.floor(self.size/2)-1,-1,-1):
            self.max_heapify(i)

    def get_parent(self, index):
        return math.floor((index+1)/2) -1
    
    def get_left(self, index):
        return 2*(index+1) -1
    
    def get_right(self,index):
        return 2*(index+1)+1
    
    def extract_max(self):
        if self.size < 1:
            print("ヒープは空です")
            return None
        max = self.arr[0]
        self.arr[0] = self.arr[self.size-1]
        self.arr.pop(self.size-1)