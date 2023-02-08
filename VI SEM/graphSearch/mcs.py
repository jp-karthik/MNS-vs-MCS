# MCS - Maximum Cardinality Search
class MCS:

    # constructor
    def __init__(self, V:int, E:int, edges:list[list]) -> None: 

        self.V = V # number of vertices
        self.E = E # number of edges
        self.edges = edges # list of edges
        self.adjList = [[] for i in range(V)] # adjacency list
        self.MCSsets = [set([]) for i in range(V)] # MCS sets for each vertex
        self.MCS_orderings = set([]) # set of all possible MCS orderings
        self.vis = [False for i in range(V)] # visited array for MCS algorithm

        # create adjacency list
        for edge in edges:
            self.adjList[edge[0]].append(edge[1])
            self.adjList[edge[1]].append(edge[0])
    
    # check if a set corresponding to a vertex (u) has maximum cardinality
    def isSetMaximumCardinality(self, u:int) -> bool:

        mxSize = 0 # maximum size of all the unvisited vertices set
        
        # loop over all vertices in the graph which are not visited yet
        for node in range(self.V):
            if self.vis[node]==False:
                mxSize = max(mxSize, len(self.MCSsets[node])) # update the maximum size of all the unvisited vertices set

        # if the size of the set corresponding to the vertex is equal to the maximum size of all the unvisited vertices set, then it is a maximum cardinality set
        return True if len(self.MCSsets[u])==mxSize else False 
    
    def performMCS(self, currentOrdering:list) -> None: # perform MCS algorithm

        # if all vertices are visited, then add the current ordering to the set of all possible MCS orderings
        if len(currentOrdering)==self.V:
            self.MCS_orderings.add(tuple(currentOrdering))
            return
        
        # loop over all vertices in the graph which are not visited yet to find the next vertex which has maximum cardinality set
        for node in range(self.V):

            if self.vis[node]==False:

                if len(self.MCSsets[node])>0 and self.isSetMaximumCardinality(node): # if the set corresponding to the vertex has maximum cardinality, then add it to the current ordering
                    
                    # mark the vertex as visited and add it to the current ordering
                    self.vis[node]=True
                    currentOrdering.append(node)
                    
                    # add the current label to the MCS sets of all the neighbours of the vertex which are not visited yet
                    for neighbour in self.adjList[node]:
                        if self.vis[neighbour]==False:
                            self.MCSsets[neighbour].add(len(currentOrdering))
                    
                    # perform MCS algorithm on the remaining vertices recursively
                    self.performMCS(currentOrdering)
                    
                    # remove the current label from the MCS sets of all the neighbours of the vertex which are not visited yet
                    for neighbour in self.adjList[node]:
                        if self.vis[neighbour]==False:
                            self.MCSsets[neighbour].remove(len(currentOrdering))
                    
                    # mark the vertex as unvisited and remove it from the current ordering
                    self.vis[node]=False
                    currentOrdering.pop()

    # perform MCS algorithm on all possible orderings
    def performAllPossible(self) -> None:

        # current ordering of the vertices
        currentOrdering = []

        # loop over all vertices in the graph
        for u in range(self.V):

            # add a starter label to the MCS set of current vertex which woud be the starting vertex 
            self.MCSsets[u].add(self.V+1)

            # call the MCS algorithm 
            self.performMCS(currentOrdering)
            
            # remove the starter label from the MCS set of current vertex
            self.MCSsets[u].remove(self.V+1)

    # get the number of MCS orderings
    def getSize(self) -> int:
        # return the size of the set of all possible MCS orderings
        return len(self.MCS_orderings)