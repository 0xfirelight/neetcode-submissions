class Edge:
    def __init__(self, src: int, dst: int):
        self.src = src
        self.dst = dst


class Graph:
    
    def __init__(self):
        self.edges = []

    def addEdge(self, src: int, dst: int) -> None:
        e = Edge(src, dst)
        self.edges.append(e)


    def removeEdge(self, src: int, dst: int) -> bool:
        for i in range(len(self.edges)):
            edge = self.edges[i]
            if edge.src == src and edge.dst == dst:
                self.edges.remove(edge)
                return True
        return False

    def hasPath(self, src: int, dst: int) -> bool:
        visited = {}
        q = deque([src])

        while q:
            node = q.popleft()

            if visited.get(node):
                continue

            if node == dst:
                return True

            visited[node] = True

            for e in self.edges:
                if e.src == node:
                    q.append(e.dst)

            
        return False



