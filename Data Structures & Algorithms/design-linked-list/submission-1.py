
class Node:
    val: int
    next: Node

    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class MyLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def get(self, index: int) -> int:
        n = self.get_node(index)
        return n.val if n else -1

    def get_node(self, index: int) -> Node:
        if not self.head:
            return None

        if index == 0:
            return self.head

        curr = self.head 
        count = 0
        while curr and count != index:
            curr = curr.next
            count += 1

        return curr
        

    def addAtHead(self, val: int) -> None:
        n = Node(val=val)
        if not self.head:
            self.head = n
            self.size += 1
            return
        
        n.next = self.head
        self.head = n
        self.size += 1


    def addAtTail(self, val: int) -> None:
        if self.size == 0 or not self.head:
            self.addAtHead(val)
            return

        print('val', val)
        print('size', self.size)
        print('head', self.head.val)

        n = self.get_node(self.size-1)
        assert n is not None,  "addAtTail: previous should exist"
        print('next', n.val)
        n.next = Node(val=val)
        self.size += 1
        

    def addAtIndex(self, index: int, val: int) -> None:
        if index == 0:
            self.addAtHead(val)
            return
        if index == self.size:
            self.addAtTail(val)
            return

        node = self.get_node(index)
        prev = self.get_node(index-1)

        assert prev, "addAtIndex: previous should exit "
        if not node or not prev:
            return None

        n = Node(val=val, next=node)
        prev.next = n
        self.size += 1


    def deleteAtIndex(self, index: int) -> None:
        if index == 0:
            self.head = self.head.next
            self.size -= 1
            return

        if index > self.size - 1:
            return None

        curr = self.get_node(index)
        prev = self.get_node(index-1)
        assert prev, "deleteAtIndex: prev should exit"

        if not curr:
            return None

        prev.next = curr.next
        self.size -= 1

        

        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)