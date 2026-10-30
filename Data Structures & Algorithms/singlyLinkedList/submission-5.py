
class Node:

    def __init__(self, val, next_node=None):
        self.val = val
        self.next = next_node


class LinkedList:
    
    def __init__(self):
        self.head = Node(-1)
        self.tail = self.head

    def get(self, index: int) -> int:
        curr = self.head.next
        i = 0
        while curr:
            if i == index:
                return curr.val
            i += 1
            curr = curr.next

        return -1

    def insertHead(self, val: int) -> None:
        n = Node(val)
        # new head
        n.next = self.head.next
        self.head.next = n

        # empty tail
        if self.tail == self.head:
            self.tail = self.head.next
        

    def insertTail(self, val: int) -> None:
        n = Node(val)
        self.tail.next = n
        self.tail = self.tail.next

        # case where there's no head
        if not self.head.next:
            self.head.next = self.tail
        

    def remove(self, index: int) -> bool:
        i = 0
        curr = self.head
        while i < index and curr:
            curr = curr.next
            i += 1

        if curr and curr.next:
            if self.tail == curr.next:
                self.tail = curr
            curr.next = curr.next.next
            return True

        return False
        
    def getValues(self) -> List[int]:
        res = []
        curr = self.head.next
        while curr:
            res.append(curr.val)
            curr = curr.next
        return res
        
