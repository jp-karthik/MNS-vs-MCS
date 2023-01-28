class MCS:

    def __init__(self, v, e, edges) -> None: #constructor
        self.v = v #vertices
        self.e = e #edges
        self.adjList = [[] for i in range(v)]
        self.MCSsets = [set([]) for i in range(v)]
        self.MCS_orderings = set([])
        self.vis = [False for i in range(v)]
        for e in edges:
            self.adjList[e[0]].append(e[1])
            self.adjList[e[1]].append(e[0])
    
    def isSetMaximumCardinality(self, u) -> bool:
        mxSize = 0
        for node in range(self.v):
            if self.vis[node]==False:
                mxSize = max(mxSize, len(self.MCSsets[node]))
        return True if len(self.MCSsets[u])==mxSize else False
    
    def performMCS(self, currentOrdering) -> None:
        if len(currentOrdering)==self.v:
            self.MCS_orderings.add(tuple(currentOrdering))
            return
        for node in range(self.v):
            if self.vis[node]==False:
                if len(self.MCSsets[node])>0 and self.isSetMaximumCardinality(node):
                    self.vis[node]=True
                    currentOrdering.append(node)
                    for neighbour in self.adjList[node]:
                        if self.vis[neighbour]==False:
                            self.MCSsets[neighbour].add(len(currentOrdering))
                    self.performMCS(currentOrdering)
                    for neighbour in self.adjList[node]:
                        if self.vis[neighbour]==False:
                            self.MCSsets[neighbour].remove(len(currentOrdering))
                    self.vis[node]=False
                    currentOrdering.pop()

    def performAllPossible(self) -> None:
        currentOrdering = []
        for u in range(self.v):
            self.MCSsets[u].add(self.v+1)
            self.performMCS(currentOrdering)
            self.MCSsets[u].remove(self.v+1)

    def getSize(self):
        return len(self.MCS_orderings)