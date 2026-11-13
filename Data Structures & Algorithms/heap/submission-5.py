class MinHeap:
    
    def __init__(self):
        self.heap = []
        self.size = 0

    def push(self, val: int) -> None:
        self.heap.append(val)
        idx = self.size
        self.heapify_up(idx)
        self.size += 1

    def pop(self) -> int:
        if not self.heap:
            print("popping: no heap")
            return -1 

        top = self.heap[0]
        bottom = self.heap[-1]

        self.size -= 1
        if self.size == 0:
            self.heap = []
            return bottom

        self.heap[0] = self.heap.pop()
        self.heapify_down(0)
        print('popping heap:', self.heap)
        return top

    def heapify_up(self, idx: int):
        if idx <= 0:
            return

        parent_idx = self.parent(idx)
        if self.heap[idx] < self.heap[parent_idx]:
            self.heap[parent_idx], self.heap[idx] = self.heap[idx], self.heap[parent_idx]
            self.heapify_up(parent_idx)

    def heapify_down(self, idx: int):
        lIdx = self.left_child(idx)
        rIdx = self.right_child(idx)
        
        if idx >= self.size or lIdx >= self.size:
            return

        val = self.heap[idx]
        lValue = self.heap[lIdx]
        if rIdx >= self.size:
            print("heapify_down: hit last element")
            # last elem
            if val > lValue:
                self.heap[idx], self.heap[lIdx] = self.heap[lIdx], self.heap[idx]
            return
                
        rValue = self.heap[rIdx]
        if lValue > rValue and val > rValue:
            self.heap[idx], self.heap[rIdx] = self.heap[rIdx], self.heap[idx]
            self.heapify_down(rIdx)
        elif rValue >= lValue and val > lValue:
            self.heap[idx], self.heap[lIdx] = self.heap[lIdx], self.heap[idx]
            self.heapify_down(lIdx)


    def top(self) -> int:
        return self.heap[0] if self.heap else -1

    def heapify(self, nums: List[int]) -> None:
        self.heap = []
        self.size = 0
        for n in nums:
            self.push(n)

    def parent(self, idx: int) -> int:
        return (idx - 1) // 2

    def left_child(self, idx: int) -> int:
        return 2 * idx + 1
        
    def right_child(self, idx: int) -> int:
        return 2 * idx + 2
        
        
        