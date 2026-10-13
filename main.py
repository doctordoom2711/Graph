class Graph:
    def __init__(self, directed=False):
        self.graph = {}
        self.directed = directed

    def add_edge(self, u, v):
        if u not in self.graph: self.graph[u] = []
        if v not in self.graph: self.graph[v] = []
        self.graph[u].append(v)
        if not self.directed:
            self.graph[v].append(u)

    def print_graph(self):
        for vertex, neighbors in self.graph.items():
            print(f"{vertex} -> {', '.join(map(str, neighbors))}")

if __name__ == "__main__":
    g = Graph()
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 2)
    g.print_graph()
