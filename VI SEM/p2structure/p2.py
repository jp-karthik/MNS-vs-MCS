import sys
sys.path.append('/Users/karthikjp/Desktop/MNS-vs-MCS/VI SEM/graphSearch')

from itertools import permutations, combinations
from IG import isInteresting

def P2(V:int, g:list[list], s:tuple) -> bool:

    # g -> adjacency list, s -> sequence
    # a -> 0, b -> 1, c -> 2, d -> 3, e -> 4, f -> 5
    
    s = list(s)

    c1 = g[s[0]].count(s[1])>0 and g[s[3]].count(s[0])>0 and g[s[0]].count(s[5])>0 and g[s[1]].count(s[5])>0 and g[s[2]].count(s[4])>0 and g[s[1]].count(s[2])>0 and g[s[1]].count(s[4])>0 # all required edges
    
    c2 = g[s[5]].count(s[2])==0 and g[s[5]].count(s[4])==0 and g[s[5]].count(s[3])==0 # no edge between f and c, e, d
    
    c3 = True # no common neighbour between a and c except b
    
    c4 = True # no common neighbour between a and e except b
    
    if c1 is False or c2 is False: 
        return False
    
    for v in range(V):
        # if v is not a, b, c, e, f and v is a neighbour of a and b, return False
        if v is not s[5] and v is not s[0] and v is not s[1] and v is not s[2] and v is not s[4]:
            if g[s[0]].count(v) and g[s[1]].count(v):
                return False

    if c1 and c2: 
        # check if there is a common neighbour between a and c except b
        for node in range(V):
            if c3:
                if node!=s[1] and node!=s[0] and node!=s[2]: # (a, c)
                    if g[node].count(s[0]) and g[node].count(s[2]): # if node is a common neighbour of a and c except b
                        c3 = False
            else:
                break

        # check if there is a common neighbour between a and e except b
        for node in range(V):
            if c4:
                if node!=s[1] and node!=s[0] and node!=s[4]: # (a, e)
                    if g[node].count(s[0]) and g[node].count(s[4]): # if node is a common neighbour of a and e except b
                        c4 = False
            else:
                break

    if c1 and c2 and (c3 or c4):
        return True
    else:
        return False
    
# function to check if the graph has a P2 structure
def hasP2(V:int, adjList:list[list]) -> bool:

    vertexSet = [i for i in range(V)]
    combs = list(combinations(vertexSet, 6)) # get all possible combinations of 6 vertices

    for comb in combs: # for each combination of 6 vertices
        
        perms = list(permutations(comb)) # get all possible permutations of the 6 vertices

        for perm in perms:
            if P2(V, adjList, perm): # if the graph has a P2 structure
                return True
                
    return False