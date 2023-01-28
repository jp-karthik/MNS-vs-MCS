class MNS:
    
    def __init__(self, V, E, edges) -> None: #constructor
        self.V = V #vertices
        self.E = E #edges
        self.adjList = [[] for i in range(V)]
        self.MNSsets = [set([]) for i in range(V)]
        self.MNS_orderings = set()
        self.vis = [False for i in range(V)]
        for e in edges:
            self.adjList[e[0]].append(e[1])
            self.adjList[e[1]].append(e[0])
    
    def isSetMaximal(self, u) -> bool:
        isMaximal = True
        for node in range(self.V):
            if node==u:
                continue
            if self.vis[node]==False:
                if len(self.MNSsets[u])==len(self.MNSsets[node]):
                    continue
                isSubset=True
                for element in self.MNSsets[u]:
                    if element not in self.MNSsets[node]:
                        isSubset=False
                if isSubset==False:
                    continue
                else:
                    isMaximal=False
                    break
        return isMaximal

    def performMNS(self, currentOrdering) -> None:
        if len(currentOrdering)==self.V:
            self.MNS_orderings.add(tuple(currentOrdering))
            return
        for node in range(self.V):
            if self.vis[node]==False:
                if len(self.MNSsets[node])>0 and self.isSetMaximal(node):
                    self.vis[node]=True
                    currentOrdering.append(node)
                    for neighbour in self.adjList[node]:
                        if self.vis[neighbour]==False:
                            self.MNSsets[neighbour].add(len(currentOrdering))
                    self.performMNS(currentOrdering)
                    for neighbour in self.adjList[node]:
                        if self.vis[neighbour]==False:
                            self.MNSsets[neighbour].remove(len(currentOrdering))
                    self.vis[node]=False
                    currentOrdering.pop()
                
    def performAllPossible(self) -> None:
        currentOrdering = []
        for u in range(self.V):
            self.MNSsets[u].add(self.V+1)
            self.performMNS(currentOrdering)
            self.MNSsets[u].remove(self.V+1)

    def getSize(self):
        return len(self.MNS_orderings)