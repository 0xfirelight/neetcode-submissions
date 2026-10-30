class Deque:
    
    def __init__(self):
        self.q = []


    def isEmpty(self) -> bool:
        return len(self.q) == 0
        

    def append(self, value: int) -> None:
        self.q.append(value)
        

    def appendleft(self, value: int) -> None:
        q = [value]
        for el in self.q:
            q.append(el)
        self.q = q
        
    def pop(self) -> int:
        if not self.q:
            return -1
        return self.q.pop()

    def popleft(self) -> int:
        if not self.q:
            return -1 

        el = self.q[0]

        q = []
        for i in range(1, len(self.q)):
            q.append(self.q[i])
            
        self.q= q
        return el
        
