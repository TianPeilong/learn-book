class Graph:
    def __init__(self, v):
        self.v = v
        self.edge = 0
        self.adj = [[] for i in v]

    def count_v(self):
        return self.v
    
    def count_edge(self):
        return self.edge

    def add_edge(self, v, w):
        self.adj[v].append(w)
        self.adj[w].append(v)
        self.edge += 1

    def get_adj(self, v):
        return self.adj[v]