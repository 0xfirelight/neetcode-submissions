
class Node:

    def __init__(self, url: str, prev_node):
        self.url = url
        self.prev = prev_node
        self.next = None


class BrowserHistory:

    def __init__(self, homepage: str):
        n = Node(homepage, None)
        self.curr = self.head = n 
        

    def visit(self, url: str) -> None:
        n = Node(url, self.curr)

        if not self.head.next:
            self.head.next = n

        self.curr.next = n
        self.curr = n
        

    def back(self, steps: int) -> str:
        print('running back', steps)
        c = steps
        while c > 0 and self.curr.prev:
            c -= 1
            self.curr = self.curr.prev
            print(self.curr.url)

        return self.curr.url

        
    def forward(self, steps: int) -> str:
        c = 0
        while c < steps and self.curr.next:
            c += 1
            self.curr = self.curr.next

        return self.curr.url
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)