class Node:

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

    

class HashTable:
    
    def __init__(self, capacity: int):
        self.store = [None] * capacity
        self.size = 0
        self.capacity = capacity

    def insert(self, key: int, value: int) -> None:
        hash_key = self.hash_function(key)
        node = self.store[hash_key]

        if not node:
            self.store[hash_key] = Node(key, value)
            self.size += 1
        else:
            prev = None
            while node:
                if node.key == key:
                    node.value = value
                    return
                prev, node = node, node.next
    
            prev.next = Node(key, value)
            self.size += 1

        if self.size / self.capacity >= .5:
            self.resize()

    def get(self, key: int) -> int:
        hash_key = self.hash_function(key)
        curr = self.store[hash_key]
        while curr:
            if curr.key == key:
                return curr.value
            curr = curr.next
        
        return -1


    def remove(self, key: int) -> bool:
        # matches
        hash_key = self.hash_function(key)
        node = self.store[hash_key]

        prev = None
        while node:
            if node.key == key:
                if prev:
                    prev.next = node.next
                else:
                    self.store[hash_key] = node.next
                self.size -= 1
                return True
            prev, node = node, node.next

        return False

    def getSize(self) -> int:
        return self.size

    def getCapacity(self) -> int:
        return self.capacity

    def resize(self) -> None:
        # matches
        new_capacity = self.capacity * 2
        new_store = [None] * new_capacity

        for node in self.store:
            while node:
                key = node.key % new_capacity
                if new_store[key] is None:
                    new_store[key] = Node(node.key, node.value)
                else:
                    head = new_store[key]
                    while head.next:
                        head = head.next
                    head.next = Node(node.key, node.value)

                node = node.next

        self.capacity = new_capacity
        self.store = new_store


    def hash_function(self, key: int):
        return key % self.capacity

