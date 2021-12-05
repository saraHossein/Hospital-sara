#------------------------------------------------------patient-----------------------------------------------------
class PQ:
    class Node:
        def __init__(self, data, key:int):
            self.data = data
            self.key = key
            self.next = None
            self.prev = None
        
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def enqueue(self, data, key:int):
        assert isinstance(key, int) , "key must be intiger"

        new_node = self.Node(data, key)
        if not self.head:
            self.head = new_node
            self.tail = new_node

        else:
            temp = self.tail
            while temp.key < key:
                if not temp.prev:
                    self.head.prev = new_node
                    new_node.next = self.head
                    self.head = new_node
                    return
                temp = temp.prev


#-------------------------------------------------------Ambulance-------------------------------------------------------
class HeapAmbulance:
    class Node:
        def __init__(self, data, key:int):
            self.data = data
            self.key = key
    
    def __init__(self):
        self.arr = [None] * 200
        self.busy = [None] * 200
        self.last = 0

    def insert(self, data, key: int):
        assert isinstance(key, int), "key for heap must be intiger"
        assert self.last <= 200 , "heap is full"
        assert 0 <= self.last 

        new_node = self.Node(data, key)

        self.arr[self.last] = new_node
        if self.last == 0:
            self.last += 1
            return
        
        parent = (self.last - 1) // 2
        child = self.last

        while parent >= 0 and self.arr[child].key > self.arr[parent].key:
            self.arr[child] , self.arr[parent] = self.arr[parent] , self.arr[child]
            child = parent
            parent = (parent - 1) //2

        self.last += 1

    def pop(self):
        assert self.last >0 , "heap is empty"

        self.last -= 1
        res = self.arr[0]
        self.arr[0] = self.arr[self.last]
        self.arr[self.last] = None
        parent = 0
        left = 1
        right = 2

        while True:
            maxindex = parent
            if self.arr[left] and self.arr[left].key > self.arr[right].key:
                maxindex = left
            if self.arr[right] and self.arr[right].key > self.arr[left].key:
                maxindex = right
            if maxindex == parent:
                break
            
            self.arr[maxindex] , self.arr[parent] = self.arr[parent] , self.arr[maxindex]
            parent = maxindex
            left = (parent * 2) +1
            right = (parent * 2) + 2
        
        return res

class PQAmbulance:
    def __init__(self):
        self.heap = HeapAmbulance()

    def enqueue(self , data, key:int):
        assert isinstance(key, int), "key must be intiger"

        self.heap.insert(data, key)

    def dequeue(self):
        res = self.heap.pop()
        return res