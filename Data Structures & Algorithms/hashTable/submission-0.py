
class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    
    def __init__(self, capacity: int):
        self.size = 0
        self.capacity = capacity
        self.table = [None] * capacity

    def hash_function(self, key): 
        return key % self.capacity
        # return new key

    def insert(self, key: int, value: int) -> None:
        idx = self.hash_function(key)
        head =  self.table[idx]
        if head is None:
            self.table[idx] = Node(key, value)
            self.size += 1
        else:
            prev = None
            while head:
                if head.key == key:
                    head.value = value
                    return
                prev, head = head, head.next 

            prev.next = Node(key, value)
            self.size += 1

        if self.size >= (self.capacity * 0.5):
            self.resize()

    def get(self, key: int) -> int:
        idx = self.hash_function(key)
        head = self.table[idx]
        while head:
            if head.key == key:
                return head.value
            head = head.next

        return -1


    def remove(self, key: int) -> bool:
        idx = self.hash_function(key)
        head = self.table[idx]

        prev = None
        while head:
            if head.key == key:
                if prev:
                    prev.next = head.next
                else:
                    self.table[idx] = head.next
                self.size -= 1
                return True

            prev, head = head, head.next
        return False

        
    def getSize(self) -> int:
        return self.size

    def getCapacity(self) -> int:
        return self.capacity

    def resize(self) -> None:
        self.capacity *= 2 
        new_table = [None] * self.capacity
        for node in self.table:
            while node:
                idx = node.key % self.capacity
                if new_table[idx] is None:
                    new_table[idx] = Node(node.key, node.value)
                else:
                    head = new_table[index]
                    node.next = head
                    new_table[index] = node
                node = node.next
            
        self.table = new_table


