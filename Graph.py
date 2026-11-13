"""Assessment 3.4 - Program for Diagram 2: Graph (BFS and DFS)

Vertices are the unique letters of your Last Name. Edit EDGES so the
graph matches the one you drew on your paper (Assessment 3.3).
"""
from collections import deque

LAST_NAME = "SEGUNDINO"   # <-- change to your last name

# Set EDGES to a list like [("S","A"), ("A","N")] to copy your own drawing.
# Leave it as None to auto-connect each letter to the next one and to the
# letter two places ahead.
EDGES = None


class Graph:
    def __init__(self):
        self.adj = {}

    def add_vertex(self, v):
        self.adj.setdefault(v, [])

    def add_edge(self, a, b):
        """Undirected edge."""
        self.add_vertex(a)
        self.add_vertex(b)
        if b not in self.adj[a]:
            self.adj[a].append(b)
        if a not in self.adj[b]:
            self.adj[b].append(a)


def build_graph(name, edges=None):
    """Algorithm A: build the graph from the letters of the name."""
    letters = []
    for ch in name.upper():
        if ch not in letters:
            letters.append(ch)
    g = Graph()
    for v in letters:
        g.add_vertex(v)
    if edges is None:
        for i, v in enumerate(letters):
            for step in (1, 2):
                if i + step < len(letters):
                    g.add_edge(v, letters[i + step])
    else:
        for a, b in edges:
            g.add_edge(a, b)
    return g, letters[0]


def bfs(g, start):
    """Algorithm B: Breadth-First Search (queue + visited set)."""
    visited = {start}
    queue = deque([start])
    result = []
    while queue:
        v = queue.popleft()
        result.append(v)
        for w in g.adj[v]:
            if w not in visited:
                visited.add(w)
                queue.append(w)
    return result


def dfs(g, v, visited=None, result=None):
    """Algorithm C: Depth-First Search (recursion + visited set)."""
    if visited is None:
        visited, result = set(), []
    visited.add(v)
    result.append(v)
    for w in g.adj[v]:
        if w not in visited:
            dfs(g, w, visited, result)
    return result


if __name__ == "__main__":
    g, start = build_graph(LAST_NAME, EDGES)
    print("Graph of:", LAST_NAME.upper(), "| start vertex:", start)
    for v, neighbors in g.adj.items():
        print(f"  {v}: {', '.join(neighbors)}")
    print("BFS:", " - ".join(bfs(g, start)))
    print("DFS:", " - ".join(dfs(g, start)))