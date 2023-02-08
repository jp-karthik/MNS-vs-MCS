# MNS : Maximal Neighbourhood Search   
class MNS:

    # constructor
    def __init__(self, V:int, E:int, edges:list[list]) -> None: 
        
        self.V = V  # number of vertices
        self.E = E  # number of edges
        self.edges = edges # list of edges
        self.adjList = [[] for i in range(V)] # adjacency list
        self.MNSsets = [set([]) for i in range(V)] # MNS sets for each vertex
        self.MNS_orderings = set()  # set of all possible MNS orderings
        self.vis = [False for i in range(V)] # visited array for MNS algorithm

        # create adjacency list
        for edge in edges:
            self.adjList[edge[0]].append(edge[1])
            self.adjList[edge[1]].append(edge[0])
    
    # check if a set corresponding to a vertex (u) is maximal under set inclusion
    def isSetMaximal(self, u:int) -> bool:

        isMaximal = True # flag to check if a set is maximal

        for node in range(self.V): # loop over all vertices in the graph
            if node==u: # skip the vertex itself
                continue
            if self.vis[node]==False: # check if the vertex is not visited yet

                if len(self.MNSsets[u])==len(self.MNSsets[node]): # if the sets are of same size, then current set is still a candidate for maximal set
                    continue

                isSubset=True # flag to check if a set is a subset of another set
                for element in self.MNSsets[u]: # loop over all elements in the current set
                    if element not in self.MNSsets[node]: # if an element is not present in the other set, then current set is not a subset of the other set
                        isSubset=False # set the flag to false
                        break

                if isSubset==False:
                    continue
                else:
                    isMaximal=False # if the current set is a subset of another set, then it is not a maximal set
                    break

        return isMaximal


    def performMNS(self, currentOrdering:list) -> None: # perform MNS algorithm

        if len(currentOrdering)==self.V: # if all vertices are visited, then add the current ordering to the set of all possible MNS orderings
            self.MNS_orderings.add(tuple(currentOrdering)) 
            return
        
         # loop over all vertices in the graph to find the next vertex to be added to the current ordering which is not visited yet and is a maximal set 
        for node in range(self.V):

            if self.vis[node]==False:

                if len(self.MNSsets[node])>0 and self.isSetMaximal(node): # check if the set corresponding to the vertex is not empty and is a maximal set

                    # add the vertex to the current ordering and mark it as visited
                    self.vis[node]=True
                    currentOrdering.append(node)

                    # add the current label to the MNS sets of all neighbours of the current vertex that are not visited yet
                    for neighbour in self.adjList[node]:
                        if self.vis[neighbour]==False:
                            self.MNSsets[neighbour].add(len(currentOrdering))

                    # perform MNS algorithm on the unvisited vertices recursively
                    self.performMNS(currentOrdering)

                    # remove the current label from the MNS sets of all neighbours of the current vertex that are not visited yet
                    for neighbour in self.adjList[node]:
                        if self.vis[neighbour]==False:
                            self.MNSsets[neighbour].remove(len(currentOrdering))

                    # remove the vertex from the current ordering and mark it as unvisited (backtrack)
                    self.vis[node]=False
                    currentOrdering.pop()

    # perform MNS algorithm on all possible orderings
    def performAllPossible(self) -> None:
        
        # current ordering of vertices
        currentOrdering = []
        
        # loop over all vertices in the graph which may be the first vertex in the ordering         
        for u in range(self.V):

            # add a starter label to the MNS set of the current vertex which would be the starting vertex 
            self.MNSsets[u].add(self.V+1)

            # call the MNS algorithm 
            self.performMNS(currentOrdering)

            # remove the starter label from the MNS set of the current vertex
            self.MNSsets[u].remove(self.V+1)

    # get the number of MNS orderings
    def getSize(self) -> int:
        # return the size of the set of all possible MNS orderings
        return len(self.MNS_orderings)