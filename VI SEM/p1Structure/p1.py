import sys
sys.path.append('/Users/karthikjp/Desktop/MNS-vs-MCS/VI SEM/graphSearch')
from itertools import permutations, combinations
from IG import isInteresting

def P1(V:int, g:list[list], s:list)->bool:
    # a->0,b->1,c->2,d->3,e->4,g->adjList,s->sequence
    c1 =  g[s[3]].count(s[0])>0 and g[s[1]].count(s[0])>0 and g[s[1]].count(s[2])>0 and g[s[1]].count(s[4])>0 and g[s[2]].count(s[4])>0 # all required edges
    c2 = True # no common neighbour between a and b
    c3 = True # no common neighbour between a and c
    c4 = True # no common neighbour between a and e
    c5 = not (g[s[2]].count(s[0])>0 and g[s[4]].count(s[0])>0) # (a,c) and (a,e) is not in E(G)
    for node in range(V):
        if g[node].count(s[0])>0 and g[node].count(s[1])>0 and node!=s[2] and node!=s[4]:
            c2 = False
        if g[node].count(s[0])>0 and g[node].count(s[2])>0 and node!=s[1]:
            c3 = False
        if g[node].count(s[0])>0 and g[node].count(s[4])>0 and node!=s[1]:
            c4 = False
    finalCnd = c1 and c2 and (c3 or c4) and c5
    return True if finalCnd else False

def hasP1(V:int, E:int, adjList:list[list], edges:list[list]) -> bool:
    if isInteresting(V, E, edges):
        vertexSet = [i for i in range(V)]
        combs = list(combinations(vertexSet, 5))
        for comb in combs:
            perms = list(permutations(comb))
            for perm in perms:
                if P1(V, adjList, perm):
                    return True
        return False
    else:
        return False