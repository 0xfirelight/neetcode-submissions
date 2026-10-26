import math

class Node:
    
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.left = None
        self.right = None


class TreeMap:
    def __init__(self):
        self.head = None

    def insert(self, key: int, val: int) -> None:
        n = Node(key, val)

        if not self.head:
            self.head = n
            return

        curr = self.head
        while curr:
            if key == curr.key:
                curr.val = val
                return
            if key > curr.key:
                if not curr.right:
                    curr.right = n
                    return
                curr = curr.right
                continue
            if key < curr.key:
                if not curr.left:
                    curr.left = n
                    return
                curr = curr.left
                continue

    def get(self, key: int) -> int:
        curr = self.head
        while curr:
            if curr.key == key:
                return curr.val
            if curr.key < key:
                curr = curr.right
            else:
                curr = curr.left

        return -1


    def getMin(self) -> int:
        curr = self.head
        while curr and curr.left:
            curr = curr.left
        return curr.val if curr else -1

    def getMax(self) -> int:
        curr = self.head
        while curr and curr.right:
            curr = curr.right
        return curr.val if curr else -1

    def findMin(self, node):
        while node and node.left:
            node = node.left
        return node

    def remove(self, key: int) -> None:
        self.head = self._remove(self.head, key)

    def _remove(self, node: Node, key: int):
        if not node:
            return None

        # in left subtree
        if key < node.key:
            node.left = self._remove(node.left, key)
        # in right subtree
        elif key > node.key:
            node.right =  self._remove(node.right, key)
        else:
            if not node.left:
                return node.right
            if not node.right:
                return node.left
            succ = self.findMin(node.right)
            node.key, node.val = succ.key, succ.val
            node.right = self._remove(node.right, succ.key)
        return node

        # key == node.key



        




    def getInorderKeys(self) -> List[int]:
        res = []

        def dfs(node):
            if not node:
                return
            dfs(node.left)
            res.append(node.key)
            dfs(node.right)

        dfs(self.head)

        return res


        


