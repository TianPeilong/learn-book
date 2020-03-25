class DepthFirstSearch:
    def __init__(self, g, s):
        self.g = g
        self.s = s
        self.marked = [False for i in range(g.count_v())]

    def dfs(self, g, v):
        self.marked[v] = True
        for w in g.adj(v):
            if not self.marked[w]:
                self.dfs(g, w)
    
    