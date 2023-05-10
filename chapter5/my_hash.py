class MyNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None

    def to_string(self):
        return "(" + str(self.key) + ", " + str(self.val) + ")"


class MyHashTable:
    def __init__(self, size):
        self.tbl = [None] * size

    def __get_hash(self, key):
        return key % len(self.tbl)

    def insert(self, key, val):
        hash_val = self.__get_hash(key)

        n = MyNode(key, val)
        if self.tbl[hash_val] == None:
            self.tbl[hash_val] = n
        else:
            ptr = self.tbl[hash_val]
            while ptr.next != None:
                ptr = ptr.next

            ptr.next = n

    def delete(self, key):
        hash_val = self.__get_hash(key)
        prev_ptr = None
        ptr = self.tbl[hash_val]
        while ptr != None:
            if ptr.key == key:
                if ptr.next != None:
                    if prev_ptr != None:
                        prev_ptr.next = ptr.next
                    else:
                        self.tbl[hash_val] = ptr.next
                else:
                    if prev_ptr != None:
                        prev_ptr.next = None
                    else:
                        self.tbl[hash_val] = None
                return None
            prev_ptr = ptr
            ptr = ptr.next

    def search(self, key):
        hash_val = self.__get_hash(key)
        if self.tbl[hash_val] != None:
            ptr = self.tbl[hash_val]
            if ptr.key == key:
                return ptr
            while ptr.next != None:
                ptr = ptr.next
                if ptr.key == key:
                    return ptr
        return None

    def to_string(self):
        stringfied_tbl = ""
        for i in range(0,len(self.tbl)):
            if self.tbl[i] != None:
                stringfied_tbl += "tbl[]"
