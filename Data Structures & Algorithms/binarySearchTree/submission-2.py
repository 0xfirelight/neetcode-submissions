class Node:

    def __init__(self, key, val=None):
        self.key = key
        self.val = val
        self.left = None
        self.right = None


class TreeMap:
    
    def __init__(self):
        self.root = None

    def insert(self, key: int, val: int) -> None:
        n = Node(key=key, val=val)

        if not self.root:
            self.root = n
            return

        curr = self.root
        while curr:
            if n.key== curr.key:
                curr.val = n.val
                return
            elif n.key < curr.key:
                if curr.left:
                    curr = curr.left
                else:
                    curr.left = n
                    return
            else:
                if curr.right:
                    curr = curr.right
                else:
                    curr.right = n
                    return


    def get(self, key: int) -> int:
        curr = self.root

        while curr: 
            if key == curr.key:
                return curr.val
            
            if  key < curr.key:
                curr = curr.left
            else:
                curr = curr.right

        return -1 


    def getMin(self) -> int:
        n = self.findMin(self.root)
        return n.val if n else -1

    def findMin(self, node):
        while node and node.left:
            node = node.left
        return node

    def getMax(self) -> int:
        curr = self.root
        while curr and curr.right:
            curr = curr.right
        return curr.val if curr else -1


    def remove(self, key: int) -> None:
        self.root = self.delete_node(self.root, key)


    def delete_node(self, node: Node, key: int) -> Node:
        if not node:
            return None

        if node.key == key:
            if not node.left:
                return node.right
            if not node.right:
                return node.left

            succ = self.findMin(node.right)
            node.key, node.val = succ.key, succ.val
            node.right = self.delete_node(node.right, succ.key)
        elif key < node.key:
            node.left =  self.delete_node(node.left, key)
        else:
            node.right = self.delete_node(node.right, key)

        return node

    def getInorderKeys(self) -> List[int]:
        res = []

        def dfs(node):
            if not node:
                return

            dfs(node.left)
            res.append(node.key)
            dfs(node.right)

        dfs(self.root)

        return res





