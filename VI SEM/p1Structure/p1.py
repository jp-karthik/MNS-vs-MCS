import sys
sys.path.append('/Users/karthikjp/Desktop/MNS-vs-MCS/VI SEM/graphSearch')

from itertools import permutations, combinations # import permutations and combinations from itertools
from IG import isInteresting # import the function isInteresting from IG.py

def P1(V:int, g:list[list], s:tuple) -> bool:
    
    # a -> 0, b -> 1, c -> 2, d -> 3, e -> 4
    # g -> adjacency list, s -> sequence

    s = list(s)

    c1 =  g[s[3]].count(s[0])>0 and g[s[1]].count(s[0])>0 and g[s[1]].count(s[2])>0 and g[s[1]].count(s[4])>0 and g[s[2]].count(s[4])>0 # all required edges
    
    c2 = True # no common neighbour between a and b except c and e

    c3 = True # no common neighbour between a and c except b

    c4 = True # no common neighbour between a and e except b

    for node in range(V): # for each node in the graph

        # if the node has a and b as neighbours and the node is not c and e
        if g[node].count(s[0])>0 and g[node].count(s[1])>0 and node!=s[2] and node!=s[4]:
            c2 = False
        
        # if the node has a and c as neighbours and the node is not b
        if g[node].count(s[0])>0 and g[node].count(s[2])>0 and node!=s[1]:
            c3 = False
        
        # if the node has a and e as neighbours and the node is not b
        if g[node].count(s[0])>0 and g[node].count(s[4])>0 and node!=s[1]:
            c4 = False
            
    # if all the conditions are satisfied
    finalCnd = c1 and c2 and (c3 or c4)

    return finalCnd

# function to check if the graph has a P1 structure
def hasP1(V:int, adjList:list[list]) -> bool:
    # V -> number of vertices, E -> number of edges, adjList -> adjacency list, edges -> list of edges
    
    vertexSet = [i for i in range(V)]
    combs = list(combinations(vertexSet, 5)) # get all possible combinations of 5 vertices
    
    for comb in combs: # for each combination

        perms = list(permutations(comb)) # get all possible permutations of the combination
        
        for perm in perms: # for each permutation
            if P1(V, adjList, perm): # if the permutation satisfies the condition of P1 return True
                return True
         
    return False 