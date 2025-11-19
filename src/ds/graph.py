class Graph:
    def __init__(self):
        self._adj = {}

    def add_vertex(self, v):
        if v not in self._adj:
            self._adj[v] = set()
            return True
        return False

    def add_edge(self, u, v):
        if u not in self._adj:
            self._adj[u] = set()
        if v not in self._adj:
            self._adj[v] = set()
        self._adj[u].add(v)
        self._adj[v].add(u)
        return True

    def remove_edge(self, u, v):
        a = False
        if u in self._adj and v in self._adj[u]:
            self._adj[u].remove(v)
            a = True
        if v in self._adj and u in self._adj[v]:
            self._adj[v].remove(u)
            a = True
        return a

    def remove_vertex(self, v):
        if v not in self._adj:
            return False
        for n in list(self._adj[v]):
            self._adj[n].discard(v)
        del self._adj[v]
        return True

    def neighbors(self, v):
        if v not in self._adj:
            return []
        return list(self._adj[v])

    def bfs(self, start):
        if start not in self._adj:
            return []
        visited = set()
        q = [start]
        visited.add(start)
        order = []
        i = 0
        while i < len(q):
            u = q[i]
            i += 1
            order.append(u)
            for v in self._adj[u]:
                if v not in visited:
                    visited.add(v)
                    q.append(v)
        return order

    def dfs(self, start):
        if start not in self._adj:
            return []
        visited = set()
        order = []
        stack = [start]
        while stack:
            u = stack.pop()
            if u in visited:
                continue
            visited.add(u)
            order.append(u)
            for v in self._adj[u]:
                if v not in visited:
                    stack.append(v)
        return order

    def size(self):
        return len(self._adj)

    def has_vertex(self, v):
        return v in self._adj