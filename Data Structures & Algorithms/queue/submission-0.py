class Deque:
    
    def __init__(self):
        self.queue = []


    def isEmpty(self) -> bool:
        return len(self.queue) == 0
        

    def append(self, value: int) -> None:
        self.queue.append(value)

    def appendleft(self, value: int) -> None:
        q = [value]
        for v in self.queue:
            q.append(v)
        self.queue = q

    def pop(self) -> int:
        if len(self.queue) < 1:
            return - 1
        el = self.queue.pop()
        return el

    def popleft(self) -> int:
        if len(self.queue) < 1:
            return -1

        el = self.queue[0]
        q = []
        for i in range(1, len(self.queue)):
            q.append(self.queue[i])
        
        self.queue = q
        return el
