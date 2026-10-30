class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

class LinkedList:
    
    def __init__(self):
        self.head = None

    
    def get(self, index: int) -> int:
        i = 0
        curr = self.head

        while i < index:
            if not curr:
                return -1
            curr = curr.next
            i += 1

        return curr.val if curr else -1
        

    def insertHead(self, val: int) -> None:
        n = Node(val=val)
        n.next = self.head
        self.head = n
        

    def insertTail(self, val: int) -> None:
        n = Node(val=val)
        if not self.head:
            self.head = n
            return

        curr = self.head
        while curr.next:
            curr = curr.next

        curr.next = n
        

    def remove(self, index: int) -> bool:

        if index == 0:
            if self.head:
                self.head = self.head.next
                return True
            return False

        prev = None
        curr = self.head
        i = 0
        while curr and i != index:
            prev = curr
            curr = curr.next
            i += 1

        if not curr:
            return False 

        prev.next = curr.next
        return  True
        
        
    def getValues(self) -> List[int]:
        res = []
        curr = self.head

        while curr:
            res.append(curr.val)
            curr = curr.next

        return res
        
